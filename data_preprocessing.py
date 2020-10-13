import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

class DataPreprocessing:

  def __init__(self, posts):
    self.data = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])
    self.process_data()
    
  def process_data(self):
    self.data['Tweets'] = self.data['Tweets'].apply(self.clean_text)
    self.data['Subjectivity'] = self.data['Tweets'].apply(self.get_subjectivity)
    self.data['Polarity'] = self.data['Tweets'].apply(self.get_polarity)
    self.data['Analysis'] = self.data['Polarity'].apply(self.get_analysis)

  def clean_text(self, text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # removes @mentions
    text = re.sub(r'#', '', text) # removing the '#' symbol
    text = re.sub(r'RT[\s]+', '', text) #removing RT
    text = re.sub(r'https?:\/\/\S+', '', text) #removing the hyperlink
    return text

  def get_subjectivity(self, text):
    return TextBlob(text).sentiment.subjectivity

  def get_polarity(self, text):
    return TextBlob(text).sentiment.polarity

  def get_analysis(self, score):
    if score < 0:
      return 'Negative'
    elif score == 0:
      return 'Neutral'
    else:
      return 'Positive'

  def get_percentage_positive_tweets(self, df):
    return get_percentage_tweets(df, type_of_tweets='positive')

  def get_percentage_negative_tweets(self, df):
    return get_percentage_tweets(df, type_of_tweets='negative')

  def get_percentage_neutral_tweets(self, df):
    return get_percentage_tweets(df, type_of_tweets='neutral')

  def get_percentage_tweets(self, df, type_of_tweets):
    tweets = df[df.Analysis == type_of_tweets]
    tweets = ptweets[type_of_tweets]

    return round((tweets.shape[0] / df.shape[0]) * 100, 1)

