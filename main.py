import argparse as arg
import pandas as pd
import csv
import tweepy
from data_preprocessing import DataPreprocessing
import data_visualization as dv
import sys

def main():
    ERROR_MESSAGE = 'Error: Please enter a valid Twitter username. (ex: --name BillGates)'

    parser = arg.ArgumentParser()
    parser.add_argument('--twitter_user', nargs='?', default=None)
    parser.add_argument('--tweets', nargs='?', default=100)
    parser.add_argument('--lang', nargs='?', default='en')
    args = parser.parse_args()

    
    if args.twitter_user == None:
        sys.stdout.write(ERROR_MESSAGE + '\n')
        sys.exit(25)
    
    credentials = []
    with open('keys.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            credentials = row
            
    api = authenticate_twitter(credentials)
    posts = api.user_timeline(screen_name=args.twitter_user, count=args.tweets, lang=args.lang, tweet_mode="extended")
    data = DataPreprocessing(posts=posts)

    dv.plot_word_cloud(data.data)
    dv.plot_polarity_vs_subjectivity(data.data)
    dv.show_value_counts(data.data)

def authenticate_twitter(list):
    consumerKey = list[0]
    consumerSecret = list[1]
    accessToken = list[2]
    accessTokenSecret = list[3]

    authenticate = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
    authenticate.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(authenticate, wait_on_rate_limit=True)

    return api

if __name__ == '__main__':
    main()