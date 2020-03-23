# Imports
import json
from pymongo import MongoClient
#from bson.json_util import dumps
import csv

# Mongo Authentication

cluster = MongoClient('mongodb://bitslab:0rang3!@localhost/?authSource=admin')

# database selection
db = cluster["coronavirus_5e332abb06036301c3a1d517"]

#collection selection
tweets = db["tweets"]
bios = db['bios']

# QUERY
tweet_obj = tweets.find({"$or":[{"retweeted_status.extended_tweet.entities.hashtags.text":{"$exists":True}},{"entities.hashtags.text":{"$exists":True}}]},{"user.screen_name":1,"entities.hashtags.text":1,"retweeted_status.extended_tweet.entities.hashtags.text":1,"timestamp_ms":1,"_id":0}).limit(3)
#print("Tweet Query DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

#with open('tweets_new.txt', 'w') as outfile:
#	json.dump(tweet_obj, outfile)

bios_obj = bios.find({"$or":[{"awards.award":{"$exists":True}},{"death":{"$exists":True}}]},{"name.last":1})

#for x in tweet_obj:
#	print(x)

#with open('bios.csv', 'w') as outfile:
#	fields = ['_id', 'name.last']
#	write = csv.DictWriter(outfile, fieldnames=fields)
#	write.writeheader()
#	for records in bios_obj:  # Here we are using 'bios_obj' as an iterator
#		user_id = records['_id']
#		last_name = records['name']['last']
#		#for x in records['name']:
#		flattened_record = {'_id': user_id,'name.last': last_name}
#		write.writerow(flattened_record)

with open('tweets.csv', 'w') as outfile:
	fields = ['screen_name','timestamp','rt_hashtags']
	write = csv.DictWriter(outfile, fieldnames=fields)
	write.writeheader()
	for records in tweet_obj:  # Here we are using 'tweet_obj' as an iterator
		text_rt = []
		text_hash = []
		username = records['user']['screen_name']
		timestamp = records['timestamp_ms'] 
		try:
			for x in records['retweeted_status']['extended_tweet']['entities']['hashtags']:
				text_rt.append(x['text'])
		except:
			text_rt = None
		flattened_record = {'screen_name':username,'timestamp': timestamp, 'rt_hashtags': text_rt}
		write.writerow(flattened_record)


