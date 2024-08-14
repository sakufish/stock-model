from newsapi import NewsApiClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from datetime import datetime

nltk.download('vader_lexicon')

# modified my api key, get your own at https://newsapi.org/
newsapi = NewsApiClient(api_key='put_the_key_here!!!')

sia = SentimentIntensityAnalyzer()

def get_sentiment(stock_symbol, date):
    # only gets for one specific day
    articles = newsapi.get_everything(q=stock_symbol, from_param=date, to=date, language='en', sort_by='relevancy')
    sentiments = []
    for article in articles['articles']:
        title = article['title'] if article['title'] else ""
        description = article['description'] if article['description'] else ""
        text = title + " " + description
        sentiment = sia.polarity_scores(text)
        sentiments.append(sentiment['compound'])
    
    return sum(sentiments) / len(sentiments) if sentiments else 0
