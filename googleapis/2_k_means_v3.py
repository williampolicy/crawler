from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

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
# 输出聚类结果
for i in range(kmeans.n_clusters):
    print('Cluster %d:' % i)
    cluster_desc = tfidf_matrix[kmeans.labels_ == i].todense()
    centroid_desc = kmeans.cluster_centers_[i]
    distances = [np.linalg.norm(x - centroid_desc) for x in cluster_desc]
    desc_indices = np.argsort(distances)[::-1][:5]
    for desc_idx in desc_indices:
        print('\t%s' % descriptions[kmeans.labels_ == i].iloc[desc_idx])
    print()

