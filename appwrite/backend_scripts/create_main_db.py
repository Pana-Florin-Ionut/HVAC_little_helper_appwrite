from appwrite.id import ID
from pydantic_classes import Database_id

def create_main_db() -> Database_id:
    from helper_functions import databases
    from appwrite_data import main_db_name
    database_id = ID.unique()
    print("DB id: " + database_id)

    result = databases.create(
        database_id = database_id,
        name = main_db_name,
        enabled = True # optional
    )
    return database_id
# Define database ID and collection IDs


# def create_database():
#     try:
#         response = databases.create(
#             database_id=DATABASE_ID,
#             name="Main Database"
#         )
#         print("Database created successfully!")
#     except Exception as e:
#         print(f"Error creating database: {e}")

# def create_companies_collection():
#     try:
#         response = databases.create_collection(
#             database_id=DATABASE_ID,
#             collection_id="companies",
#             name="Companies",
#             permissions=[],
#             document_security=True
#         )
#         # Add attributes
#         databases.create_string_attribute(DATABASE_ID, "companies", "name", 255, required=True)
#         databases.create_string_attribute(DATABASE_ID, "companies", "adminId", 36, required=True)
#         databases.create_datetime_attribute(DATABASE_ID, "companies", "createdAt", required=True)
#         print("Companies collection created successfully!")
#     except Exception as e:
#         print(f"Error creating Companies collection: {e}")

# def create_users_collection():
#     try:
#         response = databases.create_collection(
#             database_id=DATABASE_ID,
#             collection_id="users",
#             name="Users",
#             permissions=[],
#             document_security=True
#         )
#         # Add attributes
#         databases.create_string_attribute(DATABASE_ID, "users", "userId", 36, required=True)
#         databases.create_string_attribute(DATABASE_ID, "users", "companyId", 36, required=True)
#         databases.create_string_attribute(DATABASE_ID, "users", "role", 36, required=True)
#         print("Users collection created successfully!")
#     except Exception as e:
#         print(f"Error creating Users collection: {e}")

# if __name__ == "__main__":
#     create_database()
#     create_companies_collection()
#     create_users_collection()
