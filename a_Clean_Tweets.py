#!/usr/bin/python

#=======================================================
#File: a_Clean_Tweets
#Cleaning Data and saving as pickle object
#using Dr Gene's Code (as given in dropbox), modified by Abishek Ganesh
#=======================================================




 
import json
import string
from pprint import pprint 
import pickle
import re


def clean_tweets(json_file,save_type='pickle'):
	'''returns a list of cleaned tweets, removes all unicode characters'''
	tweets  = json.load(open(json_file,'r'))
	tweets_list=[]
	ignrd_tweets = []
	for tweet in tweets:
		try:
			text = tweet.lower()
			text=re.sub(r'http.://[\w].co/[\w]+',r'---',text)
			# remove the punctuations and digits
			for punc in string.punctuation:
				text = text.replace(punc,' ')
			for dig in string.digits:
				text = text.replace(dig,' ')
			tweets_list.append(text)
		except UnicodeEncodeError:
			ignrd_tweets.append(tweet['text'])
			continue
	
			
	#saving as pickle file
	if save_type=='pickle':
		outfile = 'op1_{}_cleaned_tweets.pickle'.format(json_file.split('/')[-1].split('.')[0])
		pickle.dump(tweets_list,open(outfile,'wb'), protocol=2)
	
	return outfile



if __name__=='__main__':
	file_name = 'tweet_stream_location_trump_WA_OR.json'
	tweets = clean_tweets(file_name)
	
