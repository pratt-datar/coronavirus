# Imports
from pymongo import MongoClient
import pprint
try:
	cluster = MongoClient('mongodb://bitslab:0rang3!@localhost/?authSource=admin')
	print("Authentication Success")
except:
	print("Authentication Failed")


db = cluster["coronavirus_5e332abb06036301c3a1d517"]
tweets = db["tweets"]
for x in tweets.find({},{"entities.hashtags.text":1,"timestamp_ms":1,"id_str":1,"user.id":1}).limit(5):
	print(x)
print("X DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
#y = list(tweets.find_one())
#print(y)

