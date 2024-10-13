import os
from dotenv import load_dotenv
import openai
import pymongo


# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
mongo_uri = os.getenv('MONGO_URI')

# Initialize Firebase
#cred = credentials.Certificate(google_credentials_path)
#firebase_admin.initialize_app(cred)
#db = firestore.client()

# Connect to MongoDB
mongo_client = pymongo.MongoClient(mongo_uri)
mongo_db = mongo_client['Fall2024']
mongo_collection = mongo_db['HackPSU.Integral']

def generate_integral_problem():
    prompt = "Generate a definite integral problem for calculus students."
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )
    
    problem = response.choices[0].text.strip()
    return problem


def store_problem_in_mongodb(problem):
    # Insert the problem into MongoDB
    result = mongo_collection.insert_one({'problem': problem})
    print(f"Problem stored with ID: {result.inserted_id}")

# Generate and store a definite integral problem
integral_problem = generate_integral_problem()
print("Definite Integral Problem:", integral_problem)
#store_problem_in_mongodb(integral_problem)
