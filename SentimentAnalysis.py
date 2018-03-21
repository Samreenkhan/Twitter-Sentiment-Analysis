# ------------- Author -------------#
# Samreen A. Khan

# ------------- Description ------------#
# Just to practice to  compute polarity and subjectivity using Twitter API data for keyword 'Musharaf'

import tweepy
from textblob import TextBlob
import nltk

nltk.download()

consumer_key = 'ZjZ4RG1ovvkYzJG6ZED1Aexom'
consumer_secret = 'I0gt2a1RuOxp4nIOo3pUbkAfmxeqFz8uIyb5xvQnnRXrHrQD1c'

access_token = '110127223-yuOAJllHYgSvpMLXDyuDYZc1wEJzzUTvVIrQuX8X'
access_token_secret = 'uVSaW1MDAqECu2ZuhANM3Kh1iKf4722hgTOLfJ5PcJ3Ng'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) 

public_tweets = api.search('Musharaf')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
