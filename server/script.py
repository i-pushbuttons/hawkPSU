from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Connect to MongoDB
connection_string = os.getenv('MONGO_URI')
mongo_client = MongoClient(connection_string)
mongo_db = mongo_client['Fall2024']
collection = mongo_db['HackPSU.Integral']
# Retrieve the document from MongoDB
document = collection.find_one({'_id': 'Fall2024.HackPSU.Integral'})  # Adjust the query as needed

# Extract the sentence from the document
sentence = document.get('problem', '')  # Replace 'sentence_field_name' with the actual field name

# Write the sentence to test.html
with open('public/test.html', 'r') as file:
    html_content = file.readlines()

insert_index = html_content.index('<div id="problems"></div>\n')

# Insert the sentence into the HTML content
html_content.insert(insert_index, f'<p>{sentence}</p>\n')

# Write the updated HTML content back to the file
with open('public/test.html', 'w') as file:
    file.writelines(html_content)

print("Sentence inserted into test.html")