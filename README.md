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


-----
在pyhonanywhere上，完成了Crawler 的Table 与figure的展示。 很清楚。

下面，我们希望进行，数据库的建设。
可以通过Sql 对数据进行读取。
- 下面我们看能否通过爬虫，建立Sql,而后读取。
-


可否在Bash内建立一个population1的数据库
mysql -u root -p
CREATE DATABASE population1;

我们之前，用这个程序，当时是实现了数据的抓取的。

```
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 在Wikipedia页面中查找具有指定类名的表格
table = soup.find("table", {"class": "wikitable"})

data = []
for row in table.select("tr"):
    row_data = []
    for cell in row.find_all(["th", "td"]):
        row_data.append(cell.text.strip())
    data.append(row_data)

# 将数据保存为表格
df = pd.DataFrame(data)
df.to_csv("output_wiki1.csv", index=False)
```

根据您提供的源码和输出，可以看到这个版本的程序已经成功地抓取并保存了数据。我注意到这个版本与之前版本的主要区别在于抓取表格的方法。在这个版本中，您使用了 table.select("tr") 代替之前的 table.find_all("tr")。另外，这个版本同时提取了表格中的<th>和<td>元素。

您可以尝试将之前版本的代码修改为如下形式，看看是否能解决问题：

python-OK解决。使用Crawler_wiki的方法。可以

-
我们需要创建一个表。
CREATE TABLE population_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_area VARCHAR(255) NOT NULL,
    population_2023 VARCHAR(255) NOT NULL
);

---
成功! 很好！ 非常感谢。下面我们希望将本地成功的代码，移植到Pythonanywhere ,并在www.choosinglove.ai 中展示出来。我现在通过git push 而后在控制台pull下来，并安装必要的关联程序，并建立数据库，以及表。而后修改工作目录，后进行运行。
---

1.更新主文件  app.py
2.注意数据库的密码更新。

- Pythonanywere: 
1. 建立数据库
2. 建立表
3. 更改服务器数据库的名称，
- 修改用户名choosinglove。
- host=choosinglove.mysql.pythonanywhere-services.com; 
- database='choosinglove$population'
- 需要修改两处。一处是开始建立。第二处，是读取。因此需要两处。

在 PythonAnywhere 中，您可以使用 MySQL 控制台或 phpMyAdmin 来创建表。下面是两种方法的步骤：

方法一：使用 MySQL 控制台
登录到 PythonAnywhere，进入控制台。

输入 mysql -u your_username -p -h your_database_host.mysql.pythonanywhere-services.com 并按回车。将 your_username 和 your_database_host 替换为您的实际 PythonAnywhere 用户名和数据库主机名。

当提示输入密码时，输入您的数据库密码并按回车。

输入 USE population; 并按回车，以选择 population 数据库。

输入以下 SQL 语句以创建 population_data 表：

sql
Copy code
CREATE TABLE population_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_area VARCHAR(255) NOT NULL,
    population_2023 VARCHAR(255) NOT NULL
);
按回车执行 SQL 语句。此时，您应该已经成功创建了 population_data 表。

USE choosinglove$population
Database changed
mysql> CREATE TABLE population_data (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     country_area VARCHAR(255) NOT NULL,
    ->     population_2023 VARCHAR(255) NOT NULL
    -> );
Query OK, 0 rows affected (0.06 sec)

-

- 1.修正数据的连接
2. 开始搜搜一个图书网站
3. 建立一个图书网站的数据库
4. 展示各类图书(就是儿童阅读的图书-只有阅读类图书)
5. 而且或许可以绘制图书

- TIPs
sql

根据您提供的代码和问题描述，问题可能出在代码执行过程中重复插入数据。从输出结果来看，数据已经重复多次。要解决这个问题，请确保每次运行程序时先清空数据库表，然后再插入新数据。您可以在插入数据前使用以下语句：

sql
Copy code
TRUNCATE TABLE population_data;
这将清空表格并重置自增ID。将此语句添加到代码中的适当位置，以便在插入新数据之前清空表：

python
Copy code
with conn.cursor() as cursor:
    cursor.execute("TRUNCATE TABLE population_data")
conn.commit()
在插入数据之前添加上述代码片段，以便在每次运行程序时清空表格。这样，您应该能够看到正确的数据显示在网页上，而不会出现重复数据。


- tips.
您需要按照 population_2023 列进行降序排序，但是请注意这个列是字符串类型，所以需要转换为整数类型以便正确排序。您可以在 SQL 查询中使用 CAST() 函数进行转换。这是修改后的 SQL 查询：

- 完全正确。，备存 app_web_tab_fig_v9.py
线面抑制到pythonanwhere.
需要做的是：1. 完成 服务器的代表 隐藏修改。 （两处）-对应网络服务器。
2. push --pull。
3. 运行。 -WELL DONE。 非常好！
-----

完全正确，非常感谢!  过去我们展示了一个从wiki的网站上，抓取人口数据，并csv，并建立数据库，而后在网站上进行展示。已经成功。下一步，我们考虑换一种数据进行上述流程。 我们拟选择kids reading books儿童图书,作为一个数据。 因此，请帮助我给出一个具有儿童图书数据的网站或数据库，我们先来抓取下，测试下吧

-
 bk_scrape_web_read_sql_function_well_done
 -├── read_sql_v1.py
├── scrape_story_berries_simple_v5.py
└── story_list.html
can work. 
----
<span class="author main-font vcard"><a class="url fn n" href="https://www.storyberries.com/author/jade-maitre/">Jade Maitre</a></span>
</span>

<span class="author main-font vcard"><a class="url fn n" href="https://www.storyberries.com/author/andrea-kaczmarek/">Andrea Kaczmarek</a></span>
</span>

---表格清理后，就会有更新数据。否则就是增加。导致数据重复。


是的，你可以选择前5副图片进行处理。你可以使用Python的Pillow库来打开和处理图像，然后使用urlretrieve函数将处理后的图像保存到本地目录中。

-----

完成，整理下程序：
python3 scrape_story_berries_fig_v2.py 
csv: title,author,link,image_url
查看数据库:


1. 抓数据
cp scrape_story_berries_fig_v2.py 1_crawler_to_csv.py
python3 1_crawler_to_csv.py 

2. 处理和调整数据
stories_image.csv:  title,author,link,image_url

修改图片格式
stories_image.csv-->stories_image_small.csv


3. 存入数据库
python3 3_csv_to_sql.py 

4. 读取数据库
4_sql_to_html.py



<style>
    .right-image {
        float: right;
        margin-left: 50%;
    }
</style>

<!-- ... -->

<img src='{image_url}' alt='{title}' class='right-image'>



