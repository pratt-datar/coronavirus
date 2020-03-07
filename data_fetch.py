# Imports
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017/")
db = cluster["coronavirus_5e332abb06036301c3a1d517"]
tweets = db["tweets"]

x= mycol.find_one()

print(x)