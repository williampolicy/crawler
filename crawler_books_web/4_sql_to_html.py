import mysql.connector

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
cursor.execute("SELECT title, author,link, image_url FROM stories_image_small")

# Fetch all rows
rows = cursor.fetchall()

# # Loop through rows and create HTML string
# html = "<html>\n<head>\n<title>Stories</title>\n</head>\n<body>\n"
# # for row in rows:
# #     title = row[0]
# #     author = row[1]
# #     link  = row[2]
# #     image_url = row[3]
# #     html += f"<h2>{title} by {author}</h2>\n"
# #     #html += f"<img src='{link}' alt='{title}'>\n"
# #     html += f"<img src='{image_url}' alt='{title}'>\n"
# # html += "</body>\n</html>"


# # Loop through rows and create HTML string
# html = "<html>\n<head>\n<title>Stories</title>\n</head>\n<body>\n"
# for row in rows:
#     title = row[0]
#     author = row[1]
#     link = row[2]
#     image_url = row[3]
#     html += f"<h2><a href='{link}'>{title} by {author}</a></h2>\n"
#     html += f"<img src='{image_url}' alt='{title}'>\n"
# html += "</body>\n</html>"


# Loop through rows and create HTML string
html = "<html>\n<head>\n<title>Stories</title>\n<style>img { float: right; margin: 10px; }</style>\n</head>\n<body>\n"
for row in rows:
    title = row[0]
    author = row[1]
    link  = row[2]
    image_url = row[3]
    html += f"<div><h2>{title} by {author}</h2>\n"
    html += f"<a href='{link}'>Link to story</a>\n"
    html += f"<img src='{image_url}' alt='{title}'></div>\n"
html += "</body>\n</html>"

# Write HTML string to file
with open("stories.html", "w") as f:
    f.write(html)

# Close cursor and database connection
cursor.close()
db.close()
