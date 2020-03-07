# Imports
from pymongo import MongoClient

cluster = MongoClient("mongodb://127.0.0.1:27017/admin")
db = cluster["coronavirus_5e332abb06036301c3a1d517"]
tweets = db["tweets"]

x= tweets.find_one()

print(x)