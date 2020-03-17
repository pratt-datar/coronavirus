# Imports
from pymongo import MongoClient

try:
	cluster = MongoClient('mongodb://bitslab:0rang3!@localhost/?authSource=admin')
	print("Authentication Success")
except:
	print("Authentication Failed")

try:

		db = cluster["coronavirus_5e332abb06036301c3a1d517"]
		tweets = db["tweets"]

		x= tweets.find_one()

		for document in x: 
			pprint(document)
except:
	print("Try again")