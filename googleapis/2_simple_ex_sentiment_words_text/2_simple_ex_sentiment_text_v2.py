import pandas as pd

# load data
books = pd.read_csv('books.csv')
sentiment_words = pd.read_csv('sentiment_word_v2.csv')

# extract book descriptions
book_descriptions = books['Description']

# create a dictionary to hold sentiment words and their scores
sentiment_scores = dict(zip(sentiment_words['sentiment_word'], sentiment_words['score']))

# compute sentiment scores for each book description
book_sentiment_scores = []
for i, book_description in enumerate(book_descriptions):
    # split book description into words
    words = book_description.lower().split()
    # compute sentiment score for the book description
    score = sum(sentiment_scores.get(word, 0) for word in words)
    # normalize score by dividing by the number of words in the book description
    normalized_score = score / len(words)
    # append the score to the list of sentiment scores
    book_sentiment_scores.append(normalized_score)

# create a DataFrame to hold the sentiment scores
scores_df = pd.DataFrame({'Title': books['Title'], 'Sentiment Score': book_sentiment_scores})

# sort the DataFrame by sentiment score in descending order
scores_df = scores_df.sort_values(by='Sentiment Score', ascending=False)

# print the scores
print(scores_df)
