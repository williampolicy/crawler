import mysql.connector

# 连接数据库
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2019",
  database="books"
)

# 从数据库中读取数据
cursor = db.cursor()
cursor.execute("SELECT * FROM story_data")
rows = cursor.fetchall()

# 创建 HTML 页面
html = "<html>\n<head>\n<title>Story List</title>\n</head>\n<body>\n<h1>Story List</h1>\n<ul>\n"
for row in rows:
    html += "<li><h3>{}</h3>\n<p>Author: {}</p>\n<p><a href='{}'>Link</a></p></li>\n".format(row[1], row[2], row[3])
html += "</ul>\n</body>\n</html>"

# 将 HTML 页面保存为文件
with open('story_list.html', 'w') as f:
    f.write(html)
