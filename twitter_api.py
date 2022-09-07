# loading packages
import tweepy
import json
import os
from dotenv import load_dotenv

load_dotenv()

# keys
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")

# function to pull data from Twitter API
def query_twitter_id(tweet_ids, file_path):
    '''
    query_twitter_id: function that gets favorite counts and retweet counts using the tweet id provided and stores it in a json file.

    Args:
        tweet_ids (int): Unique identifier for the tweets.
        file_path (str): Path to store the file generated from the output.
    
    Returns:
        file: A file that contains the tweet id, favorite count and retweet count for each tweet.

    '''
    # API authentication
    auth = tweepy.OAuthHandler(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret
    )
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    tweet = {"tweet_id": [], "retweet_count": [], "favorite_count": []}
    fail = []
    
    for tweet_id in tweet_ids:
        try:
            status = api.get_status(tweet_id, tweet_mode='extended')
            tweet["tweet_id"].append(int(tweet_id))
            tweet["favorite_count"].append(int(status.favorite_count))
            tweet["retweet_count"].append(int(status.retweet_count))
            # saving file as json
            with open(file_path, 'w') as outfile:
                json.dump(tweet, outfile, indent=4)
                
        except:
            fail.append(tweet_id)
            pass
    print(fail)
    print('done')