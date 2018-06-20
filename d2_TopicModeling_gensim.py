#!/bin/lib/python


#=======================================================
#d2_TopicModeling_gensim
#Cleaning Data and generating topics using Gensim
#using Dr Gene's Code (as given in dropbox), modified by Abishek Ganesh
#=======================================================



from gensim import corpora, models, similarities, matutils
import re
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import  CountVectorizer
import json
import pickle
# for logging
import logging
import string
from pprint import pprint
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
ls = LancasterStemmer()
        

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO


def callgensim(file_name, num_topics, runs):

        tweets =pickle.load(open(file_name,'rb'))
        print(type(tweets))
        
        
        docs = []

        stopwords = nltk.corpus.stopwords.words('english')+[u'rt',u'donald',u'trump',u'tweet', u'retweet', u'realdonaldtrump', 'tweet']


        for tweet in tweets:
            twet_cln = []
            for word in tweet.split():
                if word not in stopwords:
                    twet_cln.append(word)
                                
            docs.append(twet_cln)
        
        
        print('Gensim data')
        
        
        from gensim import corpora
        dic  = corpora.Dictionary(docs)
        print(dic)
        corpus = [dic.doc2bow(text) for text in docs]
        
        
        
        from gensim import models
        tfidf = models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]
        
        
        
        print('-----'*100)
        NUM_TOPICS = num_topics
        print(NUM_TOPICS,runs)
        
        
        print('Working on LDA Model')
        model = models.ldamodel.LdaModel(corpus_tfidf, num_topics=NUM_TOPICS, id2word=dic, update_every=1, passes=runs)
        
        
        # Printing Topics found
        print(model.log_perplexity(corpus))
        topics_found = model.print_topics(10)
        counter = 1
        for t in topics_found:
                print('Topic #{} {}'.format(counter, t))
                counter+=1
        with open('gensim output_{}_{}_{}.txt'.format(runs, NUM_TOPICS, file_name.split()[0]), 'w') as f:
                f.write('model Perplexity: {}\n'.format(model.log_perplexity(corpus)))
                for i in model.print_topics(NUM_TOPICS):
                        f.write('{}'.format(i))
        print('------'*100)
        
        
        
        
if __name__ == '__main__':
        callgensim('op1_tweet_stream_location_trump_Texas_cleaned_tweets.pickle', 5, 500)