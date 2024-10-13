import os
from dotenv import load_dotenv
import openai
import firebase_admin
from firebase_admin import credentials, firestore

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
google_credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Initialize Firebase
cred = credentials.Certificate(google_credentials_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

def generate_integral_problem():
    prompt = "Generate a definite integral problem for calculus students."
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )
    
    problem = response.choices[0].text.strip()
    return problem

#def store_problem_in_firebase(problem):
 #   doc_ref = db.collection('integral_problems').add({
  #      'problem': problem
  #  })
  #  print(f"Problem stored with ID: {doc_ref.id}")

# Generate and store a definite integral problem
integral_problem = generate_integral_problem()
print("Definite Integral Problem:", integral_problem)
#store_problem_in_firebase(integral_problem)
