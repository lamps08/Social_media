#=======================================================
#d2_TopicModeling_gensim
#Calling all functions for the analysis
#using Dr Gene's Code (as given in dropbox), modified by Abishek Ganesh
#=======================================================


#python3 
from a_Clean_Tweets import clean_tweets
from b_Sentiment_Analysis import generate_hist
from c_Wordcloud import generate_wordcloud
from d1_TopicModeling import generate_topics_NMF

save_loc = clean_tweets('tweet_stream_trump.json')
state = 'All States'
generate_hist(save_loc, state)
generate_wordcloud(save_loc, state)
generate_topics_NMF(save_loc, state,10)


'''

tweet_stream_location_trump_CA.json
tweet_stream_location_trump_CO.json
tweet_stream_location_trump_Misc.json
tweet_stream_location_trump_Texas.json
tweet_stream_location_trump_WA_OR.json
tweet_stream_trump.json



'''