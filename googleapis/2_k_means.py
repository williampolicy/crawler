import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 读取书籍数据
books_df = pd.read_csv('books.csv')

print(books_df)
print('-------')

# 将书名这一列从数据中删除
book_titles = books_df.pop('Title')

# 初始化MinMaxScaler对象
scaler = MinMaxScaler()

# 将Published Date这一列从数据中删除
books_df.pop('Published Date')

# 将Description这一列从数据中删除
#books_df.pop('Description')

# 将Author这一列从数据中删除
books_df.pop('Author')

print(books_df)

# 将缩放后的数据转换为DataFrame格式
df_scaled = pd.DataFrame(scaler.fit_transform(books_df), columns=books_df.columns)


# 将书名这一列加回来
df_scaled.insert(0, 'Title', book_titles)

# 输出缩放后的数据
print(df_scaled.head())

# 标准化数据
scaler = StandardScaler()
df_scaled.drop('Title', axis=1, inplace=True)
df_scaled = scaler.fit_transform(df_scaled)

# 降维
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)

# 使用K-Means聚类算法
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df_scaled)
labels = kmeans.labels_

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(df_pca[:, 0], df_pca[:, 1], c=labels)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Book Clusters')
plt.show()

# 将聚类结果加入数据中
df_scaled = pd.DataFrame(df_scaled, columns=books_df.columns)
df_scaled.insert(0, 'Title', book_titles)
df_scaled['Cluster'] = labels

# 输出聚类结果
print(df_scaled[['Title', 'Author', 'empathy_score', 'free_will_score', 'Cluster']].sort_values(by='Cluster'))
