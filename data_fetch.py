# Imports
from pymongo import MongoClient
#import urllib.parse

#username = urllib.parse.quote_plus('pdatar')
#password = urllib.parse.quote_plus('joshist800')

try:

	cluster = MongoClient('mongodb://%s:%s@127.0.0.1' % ('bitslab', '0rang3!'))
	print("M1 success")
except:
	print("Percent-Escaping Username and Password failed")

try:
	cluster = MongoClient('mongodb://bitslab:0rang3!@localhost/?authSource=admin')
	print("M2 Success")
except:
	print("stackoverflow method failed")

try:
	cluster = MongoClient(host=['localhost:27017'],username='bitslab',password='0rang3!',authSource='admin',authMechanism='SCRAM-SHA-256')
	print("M3 Success")
except:
	print("M3 failed")

#cluster = MongoClient("mongodb://127.0.0.1:27017/admin")
try:

		db = cluster["coronavirus_5e332abb06036301c3a1d517"]
		tweets = db["tweets"]

		x= tweets.find_one()

		print(x)
except:
	print("Try again")