# crawler
crawler 


然后，您可以使用以下Python代码将CSV文件的数据插入MySQL数据库：

python
Copy code
import csv
import pymysql

# 替换以下值以连接到您的MySQL数据库
db_host = "localhost"
db_user = "your_username"
db_password = "your_password"
db_name = "your_database"

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
注意，您需要将db_host、db_user、db_password和db_name替换为您自己的MySQL数据库设置。这段代码将创建一个名为population_data的新表（如果尚不存在），然后从CSV文件中读取数据并将其插入数据库。

在运行此代码之前，请确保您已创建一个数据库并授予用户足够的权限。如果您需要创建一个新的数据库，可以使用以下命令：

sql
Copy code
CREATE DATABASE your_database;
GRANT ALL PRIVILEGES ON your_database.* TO 'your_username'@'localhost';
现在，您应该能够将CSV文件的数据插入到MySQL数据库中了。如果您在使用过程中遇到任何问题，请随时告诉我。

--
数据库名称，以及
CREATE DATABASE your_database_name;
CREATE DATABASE educationarlington;

brew services start mysql
mysqladmin -u root password '***9‘
-
mysqladmin -u root password 'your_password'
mysql -u root -p

---

进入数据库
mysql -u root -p '***9‘
-

CREATE DATABASE population;
GRANT ALL PRIVILEGES ON population.* TO 'your_username'@'localhost';
GRANT ALL PRIVILEGES ON population.* TO root@'localhost';

-进入数据库查看，
mysql -u root -p

USE population;

SELECT * FROM population_data;

SELECT * FROM population_data LIMIT 10;

从查询结果来看，数据已经成功转存到MySQL数据库中。但是，请注意，表格的第一行似乎包含了CSV文件的标题。您可能需要删除该行，以便只保留实际的国家/地区数据。要删除包含CSV标题的行，请执行以下SQL命令：
sql
Copy code
DELETE FROM population_data WHERE id = 1;
执行完这个命令后，可以再次使用 SELECT * FROM population_data LIMIT 10; 命令来查看表格中的数据，确认标题行已被删除。


-----
1. 抓取数据库； crawler_wiki.py   --> csv
2. 将数据转为sql结构，   csv2 sql
3. 读取Sql 数据

python3 readsql_table_fig.py 
完成，
下面移植

为方便起见，我们整合一下：
将抓取数据、数据转为Sql语言，读取sql文件都按照Flask的结构完成
-完成1：output_wiki.csv-->app_tab_fig_v3.py  OK.
下面我们读取Sql 看是否可以。
-push 一下. 



