import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# load data
books = pd.read_csv('books.csv')
reader_input = input("Please enter your preferences: ")

# extract book descriptions
book_descriptions = books['Description']

# initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# compute TF-IDF weights for each word in the book descriptions
tfidf_matrix = tfidf_vectorizer.fit_transform(book_descriptions)

# get TF-IDF vectorizer feature names
tfidf_feature_names = tfidf_vectorizer.get_feature_names_out()

# split reader input into words
reader_words = reader_input.lower().split()

# create a dictionary to hold reader sentiment words and their scores
reader_sentiment_scores = {}
for word in reader_words:
    reader_sentiment_scores[word] = 1.0

# create a DataFrame to hold the reader sentiment scores
reader_scores_df = pd.DataFrame({'sentiment_word': list(reader_sentiment_scores.keys()), 
                                 'score': list(reader_sentiment_scores.values())})

# append the reader sentiment scores to the original sentiment words DataFrame
sentiment_words = pd.concat([pd.read_csv('sentiment_words_v1.csv'), reader_scores_df], ignore_index=True)

# compute sentiment scores for each book description
book_sentiment_scores = []
for i, book_description in enumerate(book_descriptions):
    words = book_description.lower().split()
    score = 0
    for word in words:
        sentiment_word = sentiment_words.loc[sentiment_words['sentiment_word'] == word]
        if not sentiment_word.empty:
            score += sentiment_word.iloc[0]['score']
    normalized_score = score / len(words)
    book_sentiment_scores.append(normalized_score)

# create a DataFrame to hold the sentiment scores
scores_df = pd.DataFrame({'Title': books['Title'], 'Sentiment Score': book_sentiment_scores})

# print the sentiment scores
print(scores_df)


import plotly.express as px
import pandas as pd

# 假设您已经有了包含书籍标题和情感分数的DataFrame 'scores_df'

# 创建一个气泡图
fig = px.scatter(scores_df, x='Title', y='Sentiment Score', size='Sentiment Score', text='Title', title='Book Sentiment Scores')

# 保存气泡图为HTML文件
fig.write_html('bubble_chart.html', auto_open=True)

