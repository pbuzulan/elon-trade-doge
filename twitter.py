import os
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from binance import Binance

TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']

auth = OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)

auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)


def is_retweet(data: dict) -> bool:
    return 'retweeted_status' in data


class Listener(StreamListener):
    def __init__(self, ):
        super(Listener, self).__init__()

    def on_status(self, status):
        if is_retweet(status._json): return
        msg = status.text
        if 'doge' in msg.lower() and status.author.id == 44196397:
            print(f'WOOOOOO ELON HAS TWEETED, LETS BUY!!!! here is the tweet: {msg}')
            Binance().buy()  # the big elon has spoken, BUY DOGE!!!

    def on_error(self, status_code):
        print(f'error, status_code: {status_code}')
        return False
