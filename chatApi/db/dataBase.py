from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("MONGO_URI")
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["chat_db"]

users_collection = db["users"]
threads_collection = db["threads"]