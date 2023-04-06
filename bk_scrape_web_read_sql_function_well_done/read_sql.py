import mysql.connector

# 连接数据库
cnx = mysql.connector.connect(user='root', password='2019', host='127.0.0.1', database='books')
cursor = cnx.cursor()

# 插入数据
for story in stories:
    add_story = ("INSERT INTO story_data "
                 "(title, author, link) "
                 "VALUES (%s, %s, %s)")
    data_story = (story['title'], story['author'], story['link'])
    cursor.execute(add_story, data_story)

# 确认插入
cnx.commit()

# 关闭连接
cursor.close()
cnx.close()
