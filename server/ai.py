import os
from dotenv import load_dotenv
import openai
import pymongo
#import firebase_admin
#from firebase_admin import credentials, firestore

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
    prompt = "Generate a definite integral problem for calculus students that takes at most 30 seconds. The problems should only be one sentence long and have no variables in the answers."
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )
    
    problem = response.choices[0].text.strip()
    return problem

def check_answer(problem, user_answer):
    print(f"Checking answer for problem: {problem} with user answer: {user_answer}")
    checkerprompt = f"Given the problem: {problem}, what is the correct answer?"
    prompt = f"Given the problem: {problem}, is the answer {user_answer} correct or within 3% variance of the correct answer? Respond with 'yes' or 'no'."
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=10
    )
    checkerresponse = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=checkerprompt,
        max_tokens=10
    )
    
    answer_check = response.choices[0].text.strip().lower()
    checker_answer = checkerresponse.choices[0].text.strip().lower()
    print(f"Answer check: {answer_check}")
    print(f"Checker answer: {checker_answer}")
    return answer_check == 'yes'

def store_in_mongodb(problem):
    # Insert the problem into MongoDB
    result = mongo_collection.insert_one({'problem': problem})
    print(f"Problem stored with ID: {result.inserted_id}")

# Generate and store a definite integral problem
integral_problem = generate_integral_problem()
print("Definite Integral Problem:", integral_problem)
store_in_mongodb(integral_problem)
