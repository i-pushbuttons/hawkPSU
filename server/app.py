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
class UserDataManager:
    def __init__(self, mongo_uri, db_name='UserDB', collection_name='Users'):
        self.mongo_client = pymongo.MongoClient(mongo_uri)
        self.db_name = db_name
        self.collection_name = collection_name
        self.db = self.mongo_client[self.db_name]
        self.collection = self.db[self.collection_name]

    def create_user(self, elo, name, email, password):
        # Prepare the user data
        user_data = {
            'elo': elo,
            'name': name,
            'email': email,
            'password': password
        }
        
        # Insert the user data into the MongoDB collection
        result = self.collection.insert_one(user_data)

    def get_user_json(self, user_id):
        # Find the user by user_id
        user = self.collection.find_one({'_id': user_id})
        
        if user:
            # Convert the MongoDB document to a JSON response
            user.pop('_id')  # Remove the '_id' field if you don't want it in the JSON response
            return jsonify(user)
        else:
            return jsonify({'error': 'User not found'})

app = Flask(__name__)
@app.route('/user/<user_id>')
def get_user(user_id):
    user_data_manager = UserDataManager(mongo_uri)
    return user_data_manager.get_user_json(user_id)

if __name__ == '__main__':
    app.run(port=5000)
    app.run(debug=True)