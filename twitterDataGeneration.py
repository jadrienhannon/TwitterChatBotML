# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 07:38:40 2020

@author: jadri
"""
import tensorflow as tf
import tweepy

import numpy as np
import os
import time

consumer_key = "sfO9vrG5cTmi3Q9333q8EFGia"
consumer_secret = "UEtFOSY0FQKrkTl1Q9q51oPUk5FF4Kn5iVqen0a0hBMUT9pJoN"
access_key = "1235234606900629504-JnBsV8CaNisW2jYzxM9VgwIftdYBX1"
access_secret = "VcKLsvV67hlqiHKo2jJJxwjjeApaSeu2Emf3a0cwFJ6jn"

def getTweets(username):
    
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    
    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)
    
    # Calling API
    api = tweepy.API(auth)
    
    # 200 tweets to be extracted
    tweets = api.user_timeline(screen_name=username)
    f = open("twitterData.txt","w")
    
    # Create an array of tweet information
    tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
    for j in tweets_for_csv:
        f.write("%s\n", j)
    f.close()
    
text = open('twitterData.txt', 'rb').read().decode(encoding='utf-8')
vocab = sorted(set(text))
print(vocab)

char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text])