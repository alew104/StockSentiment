# TODO:
# BUILD NLP ANALYSIS
# HAVE IT WRITE TO AZURE
# look into vader and how to extract scores
# look into vader in general
# kms
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tableaccess import TableAccess


class SentimentAnalysis():
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def return_scores(self, sentence):
        snt = self.analyzer.polarity_scores(sentence)
        return snt
