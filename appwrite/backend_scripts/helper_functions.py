from appwrite.services.databases import Databases
from appwrite_data import client
from appwrite_data import main_db_name
databases = Databases(client)

# print(databases.list())
# print(type(databases.list()))
def get_main_db_id():
    content: dict = databases.list()
    if content["total"] > 0:
        for db in content["databases"]:
            # print(db["name"])
            if db["name"] == main_db_name:
                return db["$id"]