from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
books_df = pd.read_csv('books.csv')

# 提取Description列
descriptions = books_df['Description']

# 创建TfidfVectorizer对象，并设置停用词
vectorizer = TfidfVectorizer(stop_words='english')

# 将文本数据转换为TF-IDF矩阵
tfidf_matrix = vectorizer.fit_transform(descriptions)

# 聚类分析
kmeans = KMeans(n_clusters=3, random_state=0).fit(tfidf_matrix)

# 获取每个样本所属的类别
labels = kmeans.labels_

# 获取每个样本的TF-IDF特征向量
features = tfidf_matrix.toarray()

print('-------')
print(books_df)

# 可视化聚类结果
plt.figure(figsize=(10, 8))
for i, label in enumerate(labels):
    x = features[i, 0]
    y = features[i, 1]
    plt.scatter(x, y, c=label, cmap='viridis')
    plt.annotate(books_df.iloc[i]['Title'], (x, y))

plt.xlabel('TF-IDF Feature 1')
plt.ylabel('TF-IDF Feature 2')
plt.show()
