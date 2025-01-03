from appwrite.client import Client

from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("APPWRITE_ENDPOINT")
project_id = os.getenv("APPWRITE_PROJECT_ID")
api_key = os.getenv("APPWRITE_API_KEY")
main_db_name = os.getenv("MAIN_DB_NAME")

# print("Endpoint:", endpoint)
# print("Project ID:", project_id)
# print("API Key:", api_key)
# Initialize Appwrite Client
client = Client()
client.set_endpoint(endpoint)  # Replace with your Appwrite endpoint
client.set_project(project_id)       # Replace with your project ID
client.set_key(api_key)