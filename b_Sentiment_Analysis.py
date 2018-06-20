#!/usr/bin/python
#encoding:utf-8


#=======================================================
#File: b_Sentiment_Analysis
#Cleaning Data and saving as pickle object
#using Dr Gene's Code (as given in dropbox), modified by Abishek Ganesh
#=======================================================



import json
from pprint import pprint
from textblob import TextBlob 
import matplotlib.pyplot as plt
import pickle
from my_stopwords import mystopwords
#getting data
import nltk

stopwords = nltk.corpus.stopwords.words('english') + mystopwords



def generate_hist(pickle_file, state):
	tweets=pickle.load(open(pickle_file,'rb'))
	tweets_list=[]
	for tweet in tweets:
	    cln_tweet=''
	    for wrd in tweet.split():
	        if wrd not in stopwords:
	             cln_tweet+=' '+wrd
	    tweets_list.append(cln_tweet)
	pollist=[]
	sublist=[]
	
	for lin in  range(len(tweets_list)) : 
		pollist.append(TextBlob(tweets_list[lin]).polarity)
		sublist.append(TextBlob(tweets_list[lin]).subjectivity))
		
	#Plotting Polarity score
		
	plt.hist(pollist, bins = 30, histtype='bar',rwidth=0.8,color='b')
	
	plt.title('Polarity Score vs Tweet Count Graph for {}\nAverage Polarity:{}'.format(state, (sum(pollist)/len(pollist))))
	plt.xlabel('Polarity Score -------->')
	plt.ylabel('Tweet Count(total tweet={}) -------->'.format(len(pollist)))
	plt.legend()
	plt.savefig('op2_1_polarity_{}_{}.pdf'.format(pickle_file.split('.')[0], state))
	plt.show()
	
	#Plotting Subjectivety score
	plt.hist(sublist,bins=30, histtype='bar',rwidth=0.8,color='r')
	plt.title('Subjectivity Score vs Tweet Count Graph for {}\nAverage Subjectivity:{}'.format(state, sum(sublist)/len(sublist)))
	plt.xlabel('Subjectivity Score -------->')
	plt.ylabel('Tweet Count (total tweet={}) -------->'.format(len(sublist)))
	plt.legend()
	plt.savefig('op2_2_subjectivity_{}_{}.pdf'.format(pickle_file.split('.')[0], state))
	plt.show()
	
	
	

if __name__=='__main__':
	generate_hist('op1_tweet_stream_trump_cleaned_tweets.pickle', 'ALL States')
	
	