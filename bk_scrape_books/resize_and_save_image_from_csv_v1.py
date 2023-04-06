import os
import urllib.request
from PIL import Image
import pandas as pd

# Load CSV data
df = pd.read_csv("stories_image.csv")

# Create output folder if it doesn't exist
output_folder = "./pics"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Loop through rows and resize/save images
for index, row in df.iterrows():
    image_url = row["image_url"]
    image_filename = image_url.split("/")[-1]
    output_path = os.path.join(output_folder, image_filename)

    # Set User-Agent header to avoid HTTP 403 error
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    request = urllib.request.Request(image_url, headers=headers)
    
    with urllib.request.urlopen(request) as url:
        with open(output_path, "wb") as image_file:
            image_file.write(url.read())

    image = Image.open(output_path)
    resized_image = image.resize((int(image.width / 20), int(image.height / 20)))
    resized_image.save(output_path)

    # Update image_url column in DataFrame
    df.at[index, "image_url"] = f"./pics/{image_filename}"

# Save updated DataFrame to new CSV file
df.to_csv("stories_image_small.csv", index=False)
