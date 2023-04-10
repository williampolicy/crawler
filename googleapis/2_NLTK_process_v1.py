import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

books = pd.read_csv("books.csv")


from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_sentiment_score(text):
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(text)
    return score['compound']


books['sentiment_score'] = books['Description'].apply(get_sentiment_score)

books_sorted = books.sort_values(by=['sentiment_score'], ascending=False)
print(books_sorted[['Title', 'Author', 'sentiment_score']])


