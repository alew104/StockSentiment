import tweepy #tweepy api wrapper
import settings #settings module
import keys




def main():
    """
        Tweepy oAuth handling.
        Uses settings taken from settings.py
    """
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)

    """
        Instantiate listener and filter incoming tweets to
        only select from a particular user
    """
    myStreamListener = StreamListener(api = api)
    myStream = tweepy.Stream(auth = api.auth, listener=StreamListener)
    myStream.filter(settings.stock_list)

"""
    Some weird python thing to make main work(?).
    Look into this.
"""
if __name__ == "__main__":
    main()
