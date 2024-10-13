from flask import Flask, jsonify, request
from ai import generate_integral_problem, check_answer
import pymongo
import os
from dotenv import load_dotenv
from flask_cors import CORS

  

# Load environment variables from .env file
load_dotenv()

# Connect to MongoDB
mongo_uri = os.getenv('MONGO_URI')
mongo_client = pymongo.MongoClient(mongo_uri)
mongo_db = mongo_client['Fall2024']
mongo_collection = mongo_db['HackPSU.Integral']


app = Flask(__name__)
CORS(app)

@app.route('/generate-problem', methods=['GET'])
def generate_problem():
    problem = generate_integral_problem()
    # Store the problem and answer in MongoDB
    mongo_collection.insert_one({'problem': problem,})
    return jsonify({'problem': problem})

@app.route('/check-answer', methods=['POST'])
def check_answer_route():
    user_answer = request.json.get('answer')
    # Retrieve the latest problem and answer from MongoDB
    latest_entry = mongo_collection.find().sort('_id', pymongo.DESCENDING).limit(1)[0]
    problem = latest_entry['problem']
    is_correct = check_answer(problem, user_answer)
    return jsonify({'correct': is_correct})

if __name__ == '__main__':
    app.run(port=5000)


