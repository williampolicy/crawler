import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2019",
    database="books"
)

cursor = db.cursor()

# 查询所有数据
cursor.execute("SELECT * FROM story_data")

# 获取查询结果
result = cursor.fetchall()

# 输出查询结果
for row in result:
    print(row)