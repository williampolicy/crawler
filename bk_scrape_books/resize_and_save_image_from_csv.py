import os
import urllib.request
from PIL import Image
import pandas as pd

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

# Load CSV data
df = pd.read_csv("stories_image_small.csv")

# Select first 5 images
image_urls = df.iloc[:5, -1]

# Create output folder if it doesn't exist
output_folder = "./pics"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Loop through images and resize/save
for url in image_urls:
    resize_and_save_image(url, output_folder)

# Update CSV data
df.iloc[:5, -1] = ["./pics/" + url.split("/")[-1] for url in image_urls]
df.to_csv("stories_image_small.csv", index=False)
