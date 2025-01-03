from appwrite.client import Client
from appwrite.services.databases import Databases

from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("APPWRITE_ENDPOINT")
project_id = os.getenv("APPWRITE_PROJECT_ID")
api_key = os.getenv("APPWRITE_API_KEY")

print("Endpoint:", endpoint)
print("Project ID:", project_id)
print("API Key:", api_key)
# Initialize Appwrite Client
client = Client()
client.set_endpoint(endpoint)  # Replace with your Appwrite endpoint
client.set_project(project_id)       # Replace with your project ID
client.set_key(api_key)


# Initialize Database Service
databases = Databases(client)

print(databases.list())
# def setup_database():
#     try:
#         # Create Database
#         database = databases.create(database_id='myDatabase', name='My Database')
#         print(f"Database created: {database['$id']}")

#         # Create Collection
#         collection = databases.create_collection(
#             database_id='myDatabase',
#             collection_id='users',
#             name='Users',
#             permissions=[],
#             document_security=True
#         )
#         print(f"Collection created: {collection['$id']}")

#         # Add Attributes to the Collection
#         databases.create_string_attribute('myDatabase', 'users', 'name', required=True, size=255)
#         databases.create_string_attribute('myDatabase', 'users', 'email', required=True, size=255, unique=True)
#         print("Attributes added to collection.")

#         # Add Initial Documents
#         databases.create_document(
#             'myDatabase', 'users', 'unique()', { 'name': 'Alice', 'email': 'alice@example.com' }
#         )
#         databases.create_document(
#             'myDatabase', 'users', 'unique()', { 'name': 'Bob', 'email': 'bob@example.com' }
#         )
#         print("Initial documents added.")

#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == '__main__':
#     setup_database()
