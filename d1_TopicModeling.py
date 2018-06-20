#!/usr/bin/env python


#=======================================================
#File: d1_TopicModeling
#Cleaning Data and generating topics using NMF
#using Dr Gene's Code (as given in dropbox), modified by Abishek Ganesh
#=======================================================




import numpy as np
import glob
import os
import string
import nltk
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import scipy.stats as stats
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import decomposition
from nltk.corpus import inaugural
import pickle
from my_stopwords import mystopwords
stopwords = nltk.corpus.stopwords.words('english') + mystopwords



def generate_topics_NMF(pickle_file, state, no_of_topics):
	corpus=[]
	tweet_list = pickle.load(open(pickle_file,'rb'))
	tweet_corpus=[]

    # Removing Stopwords
	for tweet in tweet_list:
	    cln_tweet=''
	    for wrd in tweet.split():
	        if wrd not in stopwords:
	             cln_tweet+=' '+wrd
	    tweet_corpus.append(cln_tweet)
    
    
    
    #NMF
	vectorizer  = TfidfVectorizer(stop_words='english', min_df=2)
	dtm = vectorizer.fit_transform(tweet_corpus)
	vocab = vectorizer.get_feature_names()
	num_topics = no_of_topics
	clf = decomposition.NMF(n_components=num_topics, random_state=1)
	doctopic = clf.fit_transform(dtm)


	topic_words = []
	num_top_words = 6
	for topic in clf.components_:
		word_idx = np.argsort(topic)[::-1][0:num_top_words]
		topic_words.append([vocab[i] for i in word_idx])
    
    #Saving	data to text file
	with open('op4_topics_{}_{}.txt'.format(pickle_file.split('.')[0], state),'w') as outfile:
		outfile.write('{}\nPossible topics in the given data are\n{}\n'.format('=='*50,'=='*50))
		for t in range(len(topic_words)):
			outfile.write('Topic {}: {}\n'.format(t+1, ' '.join(topic_words[t][:15])))




#Main
if __name__=='__main__':
	generate_topics_NMF('op1_tweet_stream_trump_cleaned_tweets.pickle', 'ALL States',10)
