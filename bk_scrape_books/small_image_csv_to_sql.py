import mysql.connector
import pandas as pd

# Load CSV data
df = pd.read_csv("stories_image_small.csv")

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2019",
    database="books"
)

# Create cursor
cursor = db.cursor()
# Create table
# Create table if it does not exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stories_image_small (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        link VARCHAR(255),
        image_url VARCHAR(255),
        image_path VARCHAR(255)
    )
""")

cursor.execute("TRUNCATE TABLE stories_image_small")

# Loop through rows and insert data into database
for index, row in df.iterrows():
    # Get values from row
    title = row["title"]
    author = row["author"]
    url = row["image_url"]
    image_url = row["image_url"].split("/")[-1]
    image_path = f"./pics/{image_url}"

    # Insert row data into database
    sql = f"INSERT INTO stories_image_small (title, author, link, image_url, image_path) VALUES ('{title}', '{author}', '{url}', '{image_url}', '{image_path}')"
    cursor.execute(sql)

    # Commit changes
    db.commit()

# # Loop through rows and update database
# for index, row in df.iterrows():
#     # Get values from row
#     title = row["title"]
#     author = row["author"]
#     url = row["image_url"]   # url 
#     image_url = row["image_url"].split("/")[-1]
#     image_path = f"./pics/{image_url}"

#     # Update database with new image path
#     sql = f"UPDATE stories_image_small SET image_path = '{image_path}' WHERE title = '{title}'"
#     cursor.execute(sql)

#     # Commit changes
#     db.commit()

# Close cursor and database connection
cursor.close()
db.close()
