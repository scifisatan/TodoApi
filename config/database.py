from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')

# Connect to the MongoDB, change the connection string per your MongoDB environment
connStr = f"mongodb+srv://{username}:{password}@cluster0.zl2lyz5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connStr)
db = client['todo_application']

collection_name = db["todos_app"]


if __name__ == "__main__":
    #test case for database connection
    print(collection_name.find_one())