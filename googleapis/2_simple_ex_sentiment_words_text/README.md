当然可以，这里给出范例。

sentiment_words.csv:

arduino
Copy code
word,score
happy,1
joy,1
amazing,1
sad,-1
anger,-1
hate,-1
text.txt:

vbnet
Copy code
I'm feeling happy and joyful today. The weather is amazing!
你可以使用下面的代码读取并测试：

python
Copy code
import pandas as pd

# 读取情感词典
sentiment_words = pd.read_csv('sentiment_words.csv')

# 读取文本
with open('text.txt', 'r') as f:
    text = f.read()

# 计算情感得分
sentiment_score = 0
for word, score in zip(sentiment_words['word'], sentiment_words['score']):
    if word in text:
        sentiment_score += score

print(sentiment_score)
输出结果应该是 3，因为文本中出现了 happy、joyful 和 amazing 这三个积极情感词，每个词的情感得分都是 1，所以总情感得分是 3。