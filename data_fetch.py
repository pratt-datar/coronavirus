# Imports
import json
from pymongo import MongoClient
import os
import csv

# Mongo Authentication

cluster = MongoClient('mongodb://bitslab:0rang3!@localhost/?authSource=admin')

# database selection
db = cluster["coronavirus_5e332abb06036301c3a1d517"]

#collection selection
tweets = db["tweets"]
#bios = db['bios']

# QUERY
#tweet_obj = tweets.find({"$or":[{"retweeted_status.extended_tweet.entities.hashtags.text":{"$exists":True}},{"entities.hashtags.text":{"$exists":True}}]},{"user.screen_name":1,"entities":1,"retweeted_status":1,"timestamp_ms":1,"_id":0})

tweet_obj = tweets.find({"$or":[{"retweeted_status.extended_tweet.entities.hashtags.text":{"$exists":True}},{"entities.hashtags.text":{"$exists":True}},{"entities.user_mentions.id":{"$exists":True}},{"retweeted_status.extended_tweet.entities.user_mentions.id":{"$exists":True}}]},{"_id":1,"id":1,"timestamp_ms":1,"entities.user_mentions.id":1,"retweeted_status.id":1,"retweeted_status.extended_tweet.entities.user_mentions.id":1,"retweeted_status.user.id":1,"user.id":1,"entities.hashtags.text":1,"retweeted_status.extended_tweet.entities.hashtags.text":1}).limit(5)

if os.path.exists('tweets_updated_v2.csv'):
	with open('tweets_updated_v2.csv', 'a',newline = '') as outfile:
		fields = ['_id','tweet_id','rt_tweetid','user','rt_user','timestamp','hashtags','rt_hashtags','mentions','rt_mentions']
		write = csv.DictWriter(outfile, fieldnames=fields)
		for records in tweet_obj:  # Here we are using 'tweet_obj' as an iterator
			rt_hashtags = []
			hashtags = []
			rt_mentions = []
			mentions = []
			user = records['user']['id']
			timestamp = records['timestamp_ms']
			unique_id = records['_id']
			tweet_id = records['id']
			try:
				rt_tweetid = records['retweeted_status']['id']
			except:
				rt_tweetid = []
			try:
				rt_user = records['retweeted_status']['user']['id']
			except:
				rt_user = []
			try:
				for x in records['retweeted_status']['extended_tweet']['entities']['hashtags']:
					rt_hashtags.append(x['text'])
				rt_hashtags = ';'.join(map(lambda x:str(x),rt_hashtags))
			except:
				rt_hashtags = []
			try:
				for y in records['entities']['hashtags']:
					hashtags.append(y['text'])
				hashtags = ';'.join(map(lambda x:str(x),hashtags))
			except:
				hashtags = []
			try:
				for z in records['retweeted_status']['extended_tweet']['entities']['user_mentions']:
					rt_mentions.append(z['id'])
				rt_mentions = ';'.join(map(lambda x:str(x),rt_mentions))
			except:
				rt_mentions = []
			try:
				for w in records['entities']['user_mentions']:
					mentions.append(w['id'])
				mentions = ';'.join(map(lambda x:str(x),mentions))
			except:
				mentions = []
			flattened_record = {'_id': unique_id, 'tweet_id': tweet_id, 'rt_tweetid': rt_tweetid, 'user': user, 'rt_user': rt_user, 'timestamp': timestamp, 'hashtags': hashtags, 'rt_hashtags': rt_hashtags, 'mentions': mentions, 'rt_mentions': rt_mentions}
			write.writerow(flattened_record)
else:
	with open('tweets_updated_v2.csv', 'w',newline = '') as outfile:
		fields = ['_id','tweet_id','rt_tweetid','user','rt_user','timestamp','hashtags','rt_hashtags','mentions','rt_mentions']
		write = csv.DictWriter(outfile, fieldnames=fields)
		write.writeheader()
		for records in tweet_obj:  # Here we are using 'tweet_obj' as an iterator
			rt_hashtags = []
			hashtags = []
			rt_mentions = []
			mentions = []
			user = records['user']['id']
			timestamp = records['timestamp_ms']
			unique_id = records['_id']
			tweet_id = records['id']
			try:
				rt_tweetid = records['retweeted_status']['id']
			except:
				rt_tweetid = []
			try:
				rt_user = records['retweeted_status']['user']['id']
			except:
				rt_user = []
			try:
				for x in records['retweeted_status']['extended_tweet']['entities']['hashtags']:
					rt_hashtags.append(x['text'])
				rt_hashtags = ';'.join(map(lambda x:str(x),rt_hashtags))
			except:
				rt_hashtags = []
			try:
				for y in records['entities']['hashtags']:
					hashtags.append(y['text'])
				hashtags = ';'.join(map(lambda x:str(x),hashtags))
			except:
				hashtags = []
			try:
				for z in records['retweeted_status']['extended_tweet']['entities']['user_mentions']:
					rt_mentions.append(z['id'])
				rt_mentions = ';'.join(map(lambda x:str(x),rt_mentions))
			except:
				rt_mentions = []
			try:
				for w in records['entities']['user_mentions']:
					mentions.append(w['id'])
				mentions = ';'.join(map(lambda x:str(x),mentions))
			except:
				mentions = []
			flattened_record = {'_id': unique_id, 'tweet_id': tweet_id, 'rt_tweetid': rt_tweetid, 'user': user, 'rt_user': rt_user, 'timestamp': timestamp, 'hashtags': hashtags, 'rt_hashtags': rt_hashtags, 'mentions': mentions, 'rt_mentions': rt_mentions}
			write.writerow(flattened_record)
