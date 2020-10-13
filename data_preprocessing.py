import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def get_subjectivity(text):
  return TextBlob(text).sentiment.subjectivity

def get_polarity(text):
  return TextBlob(text).sentiment.polarity

def get_analysis(score):
  if score < 0:
    return 'Negative'
  elif score == 0:
    return 'Neutral'
  else:
    return 'Positive'

def get_percentage_positive_tweets(df):
    return get_percentage_tweets(df, type_of_tweets='positive')

def get_percentage_negative_tweets(df):
    return get_percentage_tweets(df, type_of_tweets='negative')

def get_percentage_neutral_tweets(df):
    return get_percentage_tweets(df, type_of_tweets='neutral')

def get_percentage_tweets(df, type_of_tweets)
    tweets = df[df.Analysis == type_of_tweets]
    tweets = ptweets[type_of_tweets]

    return round((tweets.shape[0] / df.shape[0]) * 100, 1)

