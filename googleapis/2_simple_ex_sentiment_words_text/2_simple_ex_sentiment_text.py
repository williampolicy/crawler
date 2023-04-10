import pandas as pd

# 读取情感词典
sentiment_words = pd.read_csv('sentiment_words.csv')

# 读取文本
with open('text.txt', 'r') as f:
    text = f.read()

# 计算情感得分
sentiment_score = 0
for word, score in zip(sentiment_words['word'], sentiment_words['score']):
    if word in text:
        sentiment_score += score

print(sentiment_score)