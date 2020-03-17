# Imports
from pymongo import MongoClient
import pprint
try:
	cluster = MongoClient('mongodb://bitslab:0rang3!@localhost/?authSource=admin')
	print("Authentication Success")
except:
	print("Authentication Failed")


db = cluster["coronavirus_5e332abb06036301c3a1d517"]
teets = db["tweets"]
x = tweets.find_one()
for document in x: 
	pprint(document)
