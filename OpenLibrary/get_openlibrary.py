import requests
import json

# Open Library API endpoint and query parameters
url = "http://openlibrary.org/search.json"
query_params = {"q": "Harry Potter"}

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
