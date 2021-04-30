from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from tweepy import API
from tweepy import Stream

from twitter import Listener, auth


api = API(auth, wait_on_rate_limit=True,
          wait_on_rate_limit_notify=True)

listener = Listener()
stream = Stream(auth, listener)


def main():
    try:
        print('all good')
        print('Start reading... please elon post about doge :(')
        stream.filter(follow=['44196397'])  # BIG ELON twitter_id @elonmusk
    except Exception as err:
        print(err)
    finally:
        print('Done.')
        stream.disconnect()
        main()


if __name__ == '__main__':
    main()
