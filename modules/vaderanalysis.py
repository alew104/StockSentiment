# TODO:
# BUILD NLP ANALYSIS
# HAVE IT WRITE TO AZURE
# look into vader and how to extract scores
# look into vader in general
# kms
from vaderSentiment import sentiment as vaderSentiment
from tableaccess import TableAccess

class SentimentAnalysis():
    def __init__(self):
