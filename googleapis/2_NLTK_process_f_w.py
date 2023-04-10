import pandas as pd
import matplotlib.pyplot as plt

# 加载同理心和自由意志词汇词典文件
empathy_words = pd.read_csv('empathy_words.csv')
free_will_words = pd.read_csv('free_will_words.csv')

# 将词典文件转换为字典
empathy_dict = dict(zip(empathy_words['empathy_word'], empathy_words['score']))
free_will_dict = dict(zip(free_will_words['free_will_word'], free_will_words['score']))

# 读取书籍数据
books_df = pd.read_csv('books.csv')

# 计算每本书籍的同理心和自由意志得分
books_df['empathy_score'] = books_df['Description'].apply(lambda x: sum(empathy_dict.get(word, 0) for word in x.lower().split()))
books_df['free_will_score'] = books_df['Description'].apply(lambda x: sum(free_will_dict.get(word, 0) for word in x.lower().split()))

# Output book scores in a table
print(books_df[['Title', 'Author', 'empathy_score', 'free_will_score']])



# 绘制二维图
plt.scatter(books_df['free_will_score'], books_df['empathy_score'], alpha=0.5)
plt.xlabel('Free Will Score')
plt.ylabel('Empathy Score')
plt.title('Free Will vs Empathy Scores of Books')
for i, row in books_df.iterrows():
    plt.annotate(row['Title'], (row['free_will_score'], row['empathy_score']))
plt.show()
