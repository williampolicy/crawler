import mysql.connector
import csv
import mysql.connector
import pandas as pd


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2019",
  database="books"
)

cursor = db.cursor()

# Create table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS stories_image (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), link VARCHAR(255), image VARCHAR(255))")

cursor.execute("TRUNCATE TABLE stories_image")

# Load data from CSV file
with open('stories_image.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = row['title']
        author = row['author']
        link = row['link']
        image = row['image']

        # Insert data into database
        sql = "INSERT INTO stories_image (title, author, link, image) VALUES (%s, %s, %s, %s)"
        val = (title, author, link, image)
        cursor.execute(sql, val)

db.commit()





db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2019",
  database="books"
)

query = "SELECT * FROM stories_image"

df = pd.read_sql(query, con=db)

html_table = df.to_html()

with open('stories_image.html', 'w', encoding='utf-8') as f:
    f.write(html_table)

