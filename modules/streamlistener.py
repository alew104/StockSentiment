# TODO:
# Figure out how to tell which tweet is to which company
# write it to azure already
# scores are in a dict, just for reference

import tweepy
from vaderanalysis import SentimentAnalysis
from tableaccess import TableAccess


class StreamListener(tweepy.StreamListener):
    def __init__(self, api, account, azurekey):
        self.api = api
        self.analyzer = SentimentAnalysis()
        self.writer = TableAccess(account, azurekey)

    """
        @param status: The tweet that the listener found

        Listener function. Will check hashtags and delete
        if target hashtag is found
    """
    def on_status(self, status):
        score = self.analyzer.return_scores(status.text.encode('utf-8'))
        print status.text
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        #self.writer.write_to_table(stock="STOCKHERE", pos, neu, neg)

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
