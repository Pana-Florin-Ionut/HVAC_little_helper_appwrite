from create_main_db import create_main_db
from helper_functions import get_main_db_id
from helper_functions import databases

DATABASE_ID = get_main_db_id()


if __name__ == '__main__':
    if not DATABASE_ID:
        DATABASE_ID = create_main_db()
    else:
        print(databases.list())



# for database in databases.list():
    # print(database)
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
