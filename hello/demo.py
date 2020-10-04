import os
import pymongo
from pymongo import MongoClient

# this is the first app on Python
VERSION = 1.0
APP_NAME = os.getenv("APP_NAME", "default")
MONGODB_HOST = os.getenv("MONGODB_HOST", "localhost")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "test-database")

print("name: %s" % APP_NAME)
print("version: %s" % VERSION)
print("hello world!")

connectionString = 'mongodb://{0}:{1}/'.format(MONGODB_HOST, 27017)
client = MongoClient(connectionString)

db = client[MONGODB_DATABASE]

document = {
	"message": "hello world"
}

insertedId = db['test-collection'].insert_one(document).inserted_id
print(insertedId)
