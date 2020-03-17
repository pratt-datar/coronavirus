# Imports
from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('pdatar')
password = urllib.parse.quote_plus('joshist800')

try:

	cluster = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
	print("M1 success")
except:
	print("Percent-Escaping Username and Password failed")

try:
	cluster = MongoClient('mongodb://pdatar:joshist800@localhost/coronavirus_5e332abb06036301c3a1d517?authSource=admin')
	print("M2 Success")
except:
	print("stackoverflow method failed")

#cluster = MongoClient("mongodb://127.0.0.1:27017/admin")
try:

		db = cluster["coronavirus_5e332abb06036301c3a1d517"]
		tweets = db["tweets"]

		x= tweets.find_one()

		print(x)
except:
	print("Try again")