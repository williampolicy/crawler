import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 读取书籍数据
books_df = pd.read_csv('books.csv')

# 删除非数值类型的列
books_df.drop(['Title', 'Author', 'Published Date'], axis=1, inplace=True)

# 初始化MinMaxScaler对象
scaler = MinMaxScaler()

# 缩放数据
df_scaled = scaler.fit_transform(books_df)

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
df_scaled.insert(0, 'Title', books_df['Title'])
df_scaled['Cluster'] = labels

# 输出聚类结果
print(df_scaled[['Title', 'Description', 'Cluster']].sort_values(by='Cluster'))
