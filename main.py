import argparse as arg
import pandas as pd
import csv
import tweepy


def main():
    ERROR_MESSAGE = 'Error: Please enter a valid Twitter username. (ex: --name BillGates)'

    parser = arg.ArgumentParser()
    parser.add_argument('--name', nargs='?', default=None)
    parser.add_argument('--tweets', nargs='?', default=100)
    args = parser.parse_args()

    ticker = args.ticker
    if len(ticker) == 1:
        sys.stdout.write(ERROR_MESSAGE + '\n')
        sys.exit(25)
    
    credentials = []
    with open('keys.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            credentials = row
            
    print(credentials)
    api = authenticate_twitter(credentials)

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