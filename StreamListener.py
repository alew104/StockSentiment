import tweepy

class StreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    """
        @param tweet: The tweet to parse

        Extracts hashtags from a tweet.

        @return list: The list of hashtags in the tweet
    """
    def find_hashtags(self, tweet):
        text = tweet.text
        split = text.split(" ")
        hashtag_list = []
        for word in split:
            if (word.startswith("#")):
                hashtag_list.append(word)
        return hashtag_list

    """
        @param hashtag_list: The list of hashtags in a tweet

        Linear search implementation to find the target hashtag in
        the list of hashtags found within a tweet

        @return boolean: returns whether the target hashtag was found
    """
    def parse_hashtags(self, hashtag_list):
        for hashtag in hashtag_list:
            if (hashtag == settings.delete_hashtag):
                return True
        return False


    """
        @param status: The tweet that the listener found

        Listener function. Will check hashtags and delete
        if target hashtag is found
    """
    def on_status(self, status):
        print (status.text)

    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        pass

    def on_limit(self, track):
        """Called when a limitation notice arrives"""
        pass

    def on_error(self, status_code):
        """Called when a non-200 status code is returned"""
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive

    def on_timeout(self):
        """Called when stream connection times out"""
        print 'Snoozing Zzzzzz'

    def on_disconnect(self, notice):
        """Called when twitter sends a disconnect notice
        Disconnect codes are listed here:
        https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
        """
        print (notice)

    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        print (notice)
