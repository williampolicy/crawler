import requests
import json
import csv

# Google Books API endpoint and query parameters
url = "https://www.googleapis.com/books/v1/volumes"
query_params = {"q": "love", "maxResults": 10}

# Send GET request to Google Books API with query parameters
response = requests.get(url, params=query_params)

# Check if response was successful
if response.status_code == 200:
    # Parse JSON data from response
    data = json.loads(response.text)
    # Print titles, authors, published dates and descriptions of books returned by search query
    for book in data["items"]:
        volume_info = book["volumeInfo"]
        title = volume_info.get("title", "")
        authors = ", ".join(volume_info.get("authors", []))
        published_date = volume_info.get("publishedDate", "")
        description = volume_info.get("description", "")
        print(f"Title: {title}\nAuthors: {authors}\nPublished Date: {published_date}\nDescription: {description}\n")
else:
    print("Error:", response.status_code)

# Store book information in CSV file
with open('books.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Author', 'Published Date', 'Description'])
    for book in data["items"]:
        volume_info = book["volumeInfo"]
        title = volume_info.get("title", "")
        authors = ", ".join(volume_info.get("authors", []))
        published_date = volume_info.get("publishedDate", "")
        description = volume_info.get("description", "")
        writer.writerow([title, authors, published_date, description])
