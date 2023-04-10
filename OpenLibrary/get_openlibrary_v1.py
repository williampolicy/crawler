import requests
import json
import csv


# Open Library API endpoint and query parameters
url = "http://openlibrary.org/search.json"
#query_params = {"q": "Harry Potter"}

query_params = {
    "q": "Harry Potter",   # 搜索关键词，可以是书名、作者、出版年份等
    "author": "Rowling",   # 作者
    "published_date": "2000"   # 出版年份
}



# Send GET request to Open Library API with query parameters
response = requests.get(url, params=query_params)

# Check if response was successful
if response.status_code == 200:
    # Parse JSON data from response
    data = json.loads(response.text)
    # Print titles of books returned by search query
    for book in data["docs"]:
        print(book["title"])
else:
    print("Error:", response.status_code)



# 将图书信息存储为CSV文件
with open('books.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Author', 'Published Date'])
    for book in data["docs"]:
        #writer.writerow([book["title"], book["author_name"][0] if "author_name" in book else "", book["publish_date"]])
        writer.writerow([book["title"], book["author_name"][0] if "author_name" in book else "", book.get("publish_date", "")])

