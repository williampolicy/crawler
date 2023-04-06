import os
import urllib.request
from PIL import Image
import pandas as pd
import sqlite3

def resize_and_save_image(image_url, output_folder):
    # Set User-Agent header to avoid HTTP 403 error
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    request = urllib.request.Request(image_url, headers=headers)
    
    # Extract image name from URL
    image_filename = image_url.split("/")[-1]
    output_path = os.path.join(output_folder, image_filename)
    
    with urllib.request.urlopen(request) as url:
        with open(output_path, "wb") as image_file:
            image_file.write(url.read())

    image = Image.open(output_path)
    resized_image = image.resize((int(image.width / 10), int(image.height / 10)))
    resized_image.save(output_path)

def update_database(image_urls):
    # Open database connection
    conn = sqlite3.connect('storybooks.db')

    # Update records with new image URLs
    for i, url in enumerate(image_urls):
        # Extract image filename from URL
        filename = url.split("/")[-1]

        # Update database with new image URL
        query = f"UPDATE stories SET image_url = '{filename}' WHERE id = {i+1};"
        conn.execute(query)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Load CSV data
df = pd.read_csv("stories_image.csv")

# Select first 5 images
image_urls = df.iloc[:5, -1]

# Create output folder if it doesn't exist
output_folder = "./pics"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Loop through images and resize/save
for url in image_urls:
    resize_and_save_image(url, output_folder)

# Update database with new image URLs
update_database(image_urls)
