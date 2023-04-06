
import mysql.connector

# Connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2019",
    database="books"
)

# Create cursor
cursor = db.cursor()

# Select data from table
cursor.execute("SELECT title, author, image_path FROM stories_image_small")

# Fetch all rows
rows = cursor.fetchall()

# Loop through rows and create HTML string
html = "<html>\n<head>\n<title>Stories</title>\n</head>\n<body>\n"
for row in rows:
    title = row[0]
    author = row[1]
    image_path = row[2]
    html += f"<h2>{title} by {author}</h2>\n"
    html += f"<img src='{image_path}' alt='{title}'>\n"
html += "</body>\n</html>"

# Write HTML string to file
with open("stories.html", "w") as f:
    f.write(html)

# Close cursor and database connection
cursor.close()
db.close()


# import mysql.connector

# # Connect to database
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="2019",
#     database="books"
# )

# # Create cursor
# cursor = db.cursor()


# # Create cursor
# cursor = db.cursor()


# # # Select data from table
# cursor.execute("SELECT title, author, image_path FROM stories_image_small")

# # Fetch all rows
# rows = cursor.fetchall()


# # Loop through rows and create HTML string
# html = "<html>\n<head>\n<title>Stories</title>\n</head>\n<body>\n"
# for row in cursor:
#     title = row[0]
#     author = row[1]
#     image_path = row[2]
#     html += f"<h2>{title} by {author}</h2>\n"
#     html += f"<img src='{image_path}' alt='{title}'>\n"
# html += "</body>\n</html>"

# # Write HTML string to file
# with open("stories.html", "w") as f:
#     f.write(html)

# # Close cursor and database connection
# cursor.close()
# db.close()
# 这段代码中的问题可能在于for循环中的cursor，应该是需要使用rows来遍历查询结果。您可以修改为以下代码试试看：
