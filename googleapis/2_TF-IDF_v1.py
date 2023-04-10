import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# 读入books.csv文件
df = pd.read_csv("books.csv")

# 读入参考词汇和对应的得分
ref_dict = {'autonomy': 5, 'choice': 4, 'decision': 4, 'will': 3, 'independence': 3, 
            'liberty': 3, 'free': 2, 'agency': 2, 'volition': 2, 'self-determination': 2, 
            'self-governance': 1, 'self-rule': 1, 'control': 1, 'power': 1}

# 使用TfidfVectorizer计算TF-IDF值
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['Description'])

# 计算每个书籍的得分
scores = []
for i in range(X.shape[0]):
    desc_words = df['Description'][i].split()
    score = sum(ref_dict.get(word.lower(), 0) for word in desc_words)
    scores.append(score)

# 运行K-Means聚类算法
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)
kmeans.fit(X)

# 将聚类结果和得分添加到DataFrame中
df['Cluster'] = kmeans.labels_
df['Score'] = scores

# 输出聚类结果
for i in range(n_clusters):
    print(f"Cluster {i}:")
    cluster_books = df[df['Cluster'] == i]
    sorted_books = cluster_books.sort_values('Score', ascending=False)
    for j in range(sorted_books.shape[0]):
        print(f"    {sorted_books.iloc[j]['Title']}")
    print()
