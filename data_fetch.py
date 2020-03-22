# Imports
from pymongo import MongoClient

# Mongo Authentication
try:
	cluster = MongoClient('mongodb://bitslab:0rang3!@localhost/?authSource=admin')
	print("We are in!")
except:
	print("Authentication Failed")

db = cluster["coronavirus_5e332abb06036301c3a1d517"]
tweets = db["tweets"]
bios = db['bios']
#tweet_obj = tweets.find({$or:[{"retweeted_status.extended_tweet.entities.hashtags.text":{$exists:true}},{"entities.hashtags.text":{$exists:true}}]},{"user.screen_name":1,"retweeted_status.user.screen_name":1,"entities.hashtags.text":1,"retweeted_status.extended_tweet.entities.hashtags.text":1,"timestamp_ms":1})
#print("Tweet Query DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

bios_obj = bios.find({$or:[{"awards.award":{$exists:true}},{"death":{$exists:true}}]},{"name.last":1})

for x in bios_obj:
	print(x)

