import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# load data
books = pd.read_csv('books.csv')
sentiment_words = pd.read_csv('sentiment_words_v1.csv')

# extract book descriptions
book_descriptions = books['Description']

# initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# compute TF-IDF weights for each word in the book descriptions
tfidf_matrix = tfidf_vectorizer.fit_transform(book_descriptions)

# get TF-IDF vectorizer feature names
#tfidf_feature_names = tfidf_vectorizer.get_feature_names()  # 报错。 使用get_feature_names_out()
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()

# create a dictionary to hold sentiment words and their scores
sentiment_scores = dict(zip(sentiment_words['sentiment_word'], sentiment_words['score']))

# compute sentiment scores for each book description
book_sentiment_scores = []
for i, book_description in enumerate(book_descriptions):
    # split book description into words
    words = book_description.lower().split()
    # compute sentiment score for the book description
    score = sum(sentiment_scores.get(word, 0) for word in words)
    # normalize score by dividing by the number of words in the book description
    normalized_score = score / len(words)
    # append the score to the list of sentiment scores
    book_sentiment_scores.append(normalized_score)

# create a DataFrame to hold the sentiment scores
scores_df = pd.DataFrame({'Title': books['Title'], 'Sentiment Score': book_sentiment_scores})

# print the sentiment scores
print(scores_df)
