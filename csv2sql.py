import csv
import pymysql

# 替换以下值以连接到您的MySQL数据库
# db_host = "localhost"
# db_user = "root"
# db_password = "2019"
# db_name = "population"


# 配置 Pythonanywher MySQL 数据库连接
app.config['MYSQL_HOST'] = 'choosinglove.mysql.pythonanywhere-services.com'  # 替换为 PythonAnywhere 提供的 MySQL 主机名
app.config['MYSQL_USER'] = 'choosinglove'  # 替换为 PythonAnywhere 提供的 MySQL 用户名
app.config['MYSQL_PASSWORD'] = 'arlington2019'  # 替换为你在 PythonAnywhere 设置的 MySQL 密码
app.config['MYSQL_DB'] = 'choosinglove$educationarlington'  # 替换为你的 MySQL 用户名和数据库名



# 连接到MySQL数据库
connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
)

cursor = connection.cursor()

# 创建一个新表来存储数据
create_table_query = """
CREATE TABLE IF NOT EXISTS population_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_area VARCHAR(255),
    un_continental_region VARCHAR(255),
    un_statistical_subregion VARCHAR(255),
    population_2022 VARCHAR(255),
    population_2023 VARCHAR(255),
    population_change VARCHAR(255)
)
"""

cursor.execute(create_table_query)
connection.commit()

# 从CSV文件中读取数据并插入MySQL数据库
with open("output_wiki.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # 跳过标题行

    for row in csvreader:
        insert_query = f"""
        INSERT INTO population_data (
            country_area,
            un_continental_region,
            un_statistical_subregion,
            population_2022,
            population_2023,
            population_change
        )
        VALUES (
            "{row[0]}",
            "{row[1]}",
            "{row[2]}",
            "{row[3]}",
            "{row[4]}",
            "{row[5]}"
        )
        """

        cursor.execute(insert_query)
        connection.commit()

cursor.close()
connection.close()
