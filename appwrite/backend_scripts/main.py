from appwrite.client import Client
from appwrite.services.databases import Databases

# Initialize Appwrite Client
client = Client()
client.set_endpoint('http://localhost/v1')  # Replace with your Appwrite endpoint
client.set_project('6776d59f00263b242e95')       # Replace with your project ID
client.set_key('standard_4ed784b11fed884b4da2cc9eb82e034a43948360e018e96ce6c3f56be979c47814972f4a9e5247ac5be75ec14a21593e026dd965df14f21b2bd53f70edfc2cd1395d4c94a99b765028710bb8955ffdb828767038db584c57393d21a82c422a62b5355272e0743179ead686cb3aa0092a89cc1847ced21cecd7b1eed9ee90254f')


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
