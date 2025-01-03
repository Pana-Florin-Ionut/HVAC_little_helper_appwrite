from appwrite.services.databases import Databases
from appwrite_data import client
from appwrite_data import main_db_name
from appwrite.query import Query
databases = Databases(client)


def get_main_db_id():
    # Query for the database with the name 'main_db_name'
    try:
        content = databases.list(queries=[Query.equal("name", main_db_name)])
        # print(content)
        if content["total"] > 0:
            return content["databases"][0]["$id"]  # Return the ID of the first matching database
    except Exception as e:
        print(f"Error fetching database: {e}")
    return None