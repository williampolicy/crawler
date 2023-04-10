import pandas as pd

# 假设 clusters 是一个字典，其中包含聚类编号和对应书籍的列表
clusters = {
    0: ['What Love Is', 'The Psychology of Romantic Love', 'All About Love'],
    1: ['Love What Matters', 'Love & Death', 'Love 2.0'],
    2: ['Almost Like Being in Love'],
    3: ['The Love Book'],
    4: ['Love', 'Love in the Present Tense']
}

# # 创建一个空的 DataFrame
# df = pd.DataFrame(columns=['Title'])

# # 填充 DataFrame 中的每一行
# for title in set([title for cluster in clusters.values() for title in cluster]):
#     row = {'Title': title}
#     for i in range(len(clusters)):
#         row[f'Cluster_{i}'] = title in clusters.get(i, [])
#     df = df.append(row, ignore_index=True)

# # 将 DataFrame 输出到 CSV 文件中
# df.to_csv('book_clusters.csv', index=False)



# 填充 DataFrame 中的每一行
rows = []
for title in set([title for cluster in clusters.values() for title in cluster]):
    row = {'Title': title}
    for i in range(len(clusters)):
        row[f'Cluster_{i}'] = title in clusters.get(i, [])
    rows.append(row)

# 创建一个 DataFrame
df = pd.DataFrame(rows)

# 将 DataFrame 输出到 CSV 文件中
df.to_csv('book_clusters.csv', index=False)


import matplotlib.pyplot as plt
import plotly.express as px

# 从 CSV 文件中读取数据
df = pd.read_csv('book_clusters.csv')

# 创建气泡图
fig = px.scatter(
    df, 
    x='Cluster_0', 
    y='Cluster_1', 
    color='Cluster_2', 
    size='Cluster_3', 
    hover_name='Title',
    title='Book Clusters'
)

# 显示图形
fig.show()

