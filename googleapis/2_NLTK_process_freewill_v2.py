import pandas as pd
import matplotlib.pyplot as plt

# 加载自由意志词汇词典文件
free_will_words = pd.read_csv('free_will_words.csv')

# 将词典文件转换为字典
free_will_dict = dict(zip(free_will_words['free_will_word'], free_will_words['score']))


# 读取书籍数据
books_df = pd.read_csv('books.csv')

# 计算每本书籍的自由意志得分
books_df['free_will_score'] = books_df['Description'].apply(lambda x: sum(free_will_dict.get(word, 0) for word in x.lower().split()))

# 按自由意志得分从高到低对书籍进行排序
books_df.sort_values(by='free_will_score', ascending=False, inplace=True)

# 输出排序结果
print(books_df[['Title', 'Author', 'free_will_score']])


# 绘制自由意志得分的柱状图
plt.bar(books_df['Title'], books_df['free_will_score'])
plt.xticks(rotation=90)
plt.xlabel('Book Title')
plt.ylabel('Free Will Score')
plt.title('Free Will Scores of Books')
plt.show()


