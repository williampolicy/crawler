import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer

# load data
books = pd.read_csv('books.csv')
sentiment_words_v1 = pd.read_csv('sentiment_words_v1.csv')
sentiment_words_v2 = pd.read_csv('sentiment_words_v2.csv')

# extract book descriptions
book_descriptions = books['Description']

# initialize TF-IDF vectorizers for each dimension
tfidf_vectorizer_v1 = TfidfVectorizer()
tfidf_vectorizer_v2 = TfidfVectorizer()

# compute TF-IDF weights for each word in the book descriptions for each dimension
tfidf_matrix_v1 = tfidf_vectorizer_v1.fit_transform(book_descriptions)
tfidf_matrix_v2 = tfidf_vectorizer_v2.fit_transform(book_descriptions)

# get TF-IDF vectorizer feature names for each dimension
tfidf_feature_names_v1 = tfidf_vectorizer_v1.get_feature_names_out()

tfidf_feature_names_v2 = tfidf_vectorizer_v2.get_feature_names_out()

# create a dictionary to hold sentiment words and their scores for each dimension
sentiment_scores_v1 = dict(zip(sentiment_words_v1['sentiment_word'], sentiment_words_v1['score']))
sentiment_scores_v2 = dict(zip(sentiment_words_v2['sentiment_word'], sentiment_words_v2['score']))

# compute sentiment scores for each book description for each dimension
book_sentiment_scores_v1 = []
book_sentiment_scores_v2 = []
for i, book_description in enumerate(book_descriptions):
    # split book description into words
    words = book_description.lower().split()
    # compute sentiment score for the book description for each dimension
    score_v1 = sum(sentiment_scores_v1.get(word, 0) for word in words)
    score_v2 = sum(sentiment_scores_v2.get(word, 0) for word in words)
    # normalize scores by dividing by the number of words in the book description
    normalized_score_v1 = score_v1 / len(words)
    normalized_score_v2 = score_v2 / len(words)
    # append the scores to the list of sentiment scores for each dimension
    book_sentiment_scores_v1.append(normalized_score_v1)
    book_sentiment_scores_v2.append(normalized_score_v2)

# create a DataFrame to hold the sentiment scores for each dimension
scores_df = pd.DataFrame({'Title': books['Title'], 'Sentiment Score 1': book_sentiment_scores_v1, 'Sentiment Score 2': book_sentiment_scores_v2})

# plot the sentiment scores as a bubble chart
fig = px.scatter(
    scores_df, 
    x='Sentiment Score 1', 
    y='Sentiment Score 2', 
    size='Sentiment Score 1', 
    color='Sentiment Score 2', 
    hover_name='Title', 
    title='Book Sentiment Scores'
)

# show the plot
fig.show()
