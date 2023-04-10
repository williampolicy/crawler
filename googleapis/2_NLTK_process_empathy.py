import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from collections import Counter

import matplotlib.pyplot as plt


# 加载数据集
empathy_words = pd.read_csv('empathy_words.csv')

# 定义一个函数，计算文本的同理心得分
def calculate_empathy_score(text):
    # 分词
    tokens = word_tokenize(text.lower())

    # 提取词干
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in tokens]

    # 去除停用词
    tokens = [token for token in tokens if token not in stopwords.words('english')]

    # 统计同理心单词的数量
    empathy_words_count = Counter(tokens) & Counter(empathy_words['Words'])
    empathy_score = sum(empathy_words_count.values())

    return empathy_score

# 定义一个函数，将POS标记转换为WordNet词性标记
def get_wordnet_pos(token):
    tag = nltk.pos_tag([token])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

# 加载书籍数据集
books = pd.read_csv('books.csv')

# 计算每本书的同理心得分
books['empathy_score'] = books['Description'].apply(calculate_empathy_score)

# 按同理心得分进行排序
books = books.sort_values(by='empathy_score', ascending=False)

# 打印结果
print(books[['Title', 'Author', 'empathy_score']])

plt.bar(df['Title'], df['empathy_score'])
plt.xticks(rotation=90)
plt.xlabel('Book Title')
plt.ylabel('Empathy Score')
plt.title('Empathy Scores of Books')
plt.show()
