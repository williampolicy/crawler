import mysql.connector
from scrape_story_berries_simple_v5 import scrape_data

# 连接数据库
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2019',
    database='books'
)

# 获取抓取的数据
stories = scrape_data()

# 将数据写入数据库
cursor = db.cursor()
for story in stories:
    title = story['title']
    author = story['author']
    link = story['link']

    # 将数据写入数据库
    sql = "INSERT INTO story_data (title, author, link) VALUES (%s, %s, %s)"
    val = (title, author, link)
    cursor.execute(sql, val)

db.commit()

html = ""

# 从数据库中读取数据并展示
cursor.execute("SELECT * FROM story_data")
rows = cursor.fetchall()

# for row in rows:
#     print("<h3>{}</h3>".format(row[1]))
#     print("<p>Author: {}</p>".format(row[2]))
#     print("<p><a href='{}'>Link</a></p>".format(row[3]))


for row in rows:
    html += "<h3>{}</h3>".format(row[1])
    html += "<p>Author: {}</p>".format(row[2])
    html += "<p><a href='{}'>Link</a></p>".format(row[3])

with open('story_list.html', 'w') as f:
    f.write(html)
