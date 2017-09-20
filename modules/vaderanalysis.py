# TODO:
# Document this short module
# lol

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalysis():
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def return_scores(self, sentence):
        snt = self.analyzer.polarity_scores(sentence)
        return snt
