
import tweepy
from textblob import TextBlob
Tweets=['eg']
def primary(input_hashtag):
    auth = tweepy.OAuthHandler('UzjspGj8sTUsSIqMPSjisWxYw', 'fofxuCxv6AwmBL9WH86jHpJV71g3j2viTUzd5ARwkKVj0pUoJI')
    auth.set_access_token('589255307-NyulfApYo9pAAXAfvucFxIJXUCIs07x7x7EOyTg3','isGlCVxxmfDDsbBFTFurjNjyknNnkjMnfSyD5G0XT7Mo0')

    api = tweepy.API(auth,wait_on_rate_limit=True)


    N = 100                          #Number of Tweets
    Tweets = tweepy.Cursor(api.search, q=input_hashtag).items(N)
    neg = 0.0
    pos = 0.0
    neg_count = 0
    neutral_count = 0
    pos_count = 0
    for tweet in Tweets:
        # print tweet.text
        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity < 0:         #Negative
            neg += blob.sentiment.polarity
            neg_count += 1
        elif blob.sentiment.polarity == 0:      #Neutral
            neutral_count += 1
        else:                                   #Positive
            pos += blob.sentiment.polarity
            pos_count += 1
    # print "Total tweets",N
    # print "Positive ",float(pos_count/N)*100,"%"
    # print "Negative ",float(neg_count/N)*100,"%"
    # print "Neutral ",float(neutral_count/N)*100,"%"
    return [['Sentiment', 'no. of tweets'],['Positive',pos_count]
            ,['Neutral',neutral_count],['Negative',neg_count]]
def tot():
    return Tweets