
import matplotlib.pyplot as plt

import pandas as pd

# 加载同理心词汇词典文件
empathy_words = pd.read_csv('empathy_words.csv')

# 将词典文件转换为字典
empathy_dict = dict(zip(empathy_words['empathy_word'], empathy_words['score']))

# 读取书籍数据
books_df = pd.read_csv('books.csv')

# 计算每本书籍的同理心得分
books_df['empathy_score'] = books_df['Description'].apply(lambda x: sum(empathy_dict.get(word, 0) for word in x.lower().split()))

# 按同理心得分从高到低对书籍进行排序
books_df.sort_values(by='empathy_score', ascending=False, inplace=True)

# 输出排序结果
print(books_df[['Title', 'Author', 'empathy_score']])

plt.bar(books_df['Title'], books_df['empathy_score'])
plt.xticks(rotation=90)
plt.xlabel('Book Title')
plt.ylabel('Empathy Score')
plt.title('Empathy Scores of Books')
plt.show()