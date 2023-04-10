import requests
import json
import csv


# Open Library API endpoint and query parameters
url = "http://openlibrary.org/search.json"
query_params = {"q": "love", "limit": 10}

# Send GET request to Open Library API with query parameters
response = requests.get(url, params=query_params)

# Check if response was successful
if response.status_code == 200:
    # Parse JSON data from response
    data = json.loads(response.text)
    
    # Write book information to CSV file
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'Published Date', 'Description'])
        for book in data["docs"]:
            writer.writerow([
                book.get("title", ""),
                book["author_name"][0] if "author_name" in book else "",
                book.get("publish_date", ""),
                book.get("description", "")
            ])
else:
    print("Error:", response.status_code)
