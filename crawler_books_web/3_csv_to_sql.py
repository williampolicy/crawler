import mysql.connector
import pandas as pd

# Load CSV data
df = pd.read_csv("stories_image_small.csv")

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2019",
    database="Books"
)

# Create cursor
cursor = db.cursor()

cursor.execute("TRUNCATE TABLE stories_image_small")

# Insert data into table
for index, row in df.iterrows():
    title = row["title"]
    author = row["author"]
    link = row["link"]
    image_url = row["image_url"]
    #image_path = row["image_path"]
    sql = f"INSERT INTO stories_image_small (title, author, link, image_url) VALUES ('{title}', '{author}', '{link}', '{image_url}')"
    cursor.execute(sql)

# Commit changes
db.commit()

# Close cursor and database connection
cursor.close()
db.close()



# READ Data from SQL

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2019",
    database="Books"
)

# Create cursor
cursor = db.cursor()

# Select data from table
cursor.execute("SELECT * FROM stories_image_small")

# Fetch all rows
rows = cursor.fetchall()

# Print rows
for row in rows:
    print(row)

# Close cursor and database connection
cursor.close()
db.close()