import nltk
from textblob import TextBlob

# 加载文本数据
with open('love_in_the_present_tense.txt', 'r') as f:
    text = f.read()

# 对文本进行预处理，如分词、词性标注等
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

# 对文本进行情感分析
blob = TextBlob(text)
polarity = blob.sentiment.polarity

# 输出情感分析结果
print(f'The sentiment polarity of "Love in the Present Tense" is {polarity:.2f}')
