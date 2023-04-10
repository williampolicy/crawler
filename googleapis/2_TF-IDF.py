import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# 读取情感标签列表
df = pd.read_csv("sentiment_labels.csv", header=None, names=["word", "sentiment"])

# 计算每个单词的 TF-IDF 值
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["word"])

# 使用 K-Means 聚类算法
kmeans = KMeans(n_clusters=5, random_state=0)
kmeans.fit(tfidf_matrix)

# 输出聚类结果
for i, label in enumerate(kmeans.labels_):
    print(f"{df.loc[i, 'word']}: {label}")
