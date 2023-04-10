import plotly.express as px
import pandas as pd


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# 假设您已经有了包含书籍标题和情感分数的DataFrame 'scores_df'

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

import plotly.graph_objects as go
import pandas as pd

# 假设您已经有了包含书籍标题和情感分数的DataFrame 'scores_df'

# 创建一个气泡图
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=scores_df['Title'],
    y=scores_df['Sentiment Score'],
    mode='markers+text',
    text=scores_df['Title'],
    textposition='top center',
    marker=dict(
        size=scores_df['Sentiment Score'] * 500,  # 调整大小乘数以改变气泡大小
        color=scores_df['Sentiment Score'],  # 为每个气泡设置颜色
        colorscale='Viridis',  # 选择一个颜色比例尺
        showscale=True,  # 显示色度标
        colorbar=dict(title='Sentiment Score')  # 为色度标设置标题
    )
))

fig.update_layout(
    title='Book Sentiment Scores',
    xaxis=dict(title='Title'),
    yaxis=dict(title='Sentiment Score')
)

# 保存气泡图为HTML文件到static目录下
fig.write_html('./static/bubble_chart.html')


# # 创建一个气泡图
# fig = px.scatter(scores_df, x='Title', y='Sentiment Score', size='Sentiment Score', text='Title', title='Book Sentiment Scores')

# # 保存气泡图为HTML文件
# fig.write_html('./static/bubble_chart.html', auto_open=True)
