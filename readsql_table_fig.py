import pymysql
import matplotlib.pyplot as plt
from prettytable import PrettyTable

db_host = 'localhost'
db_user = 'root'
db_password = '2019'
db_name = 'population'

connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

try:
    with connection.cursor() as cursor:
        # 查询前10行数据
        sql = "SELECT * FROM population_data LIMIT 10;"
        cursor.execute(sql)
        result = cursor.fetchall()

        # 提取国家和2023年人口数据
        countries = [row[1] for row in result]
        population_2023 = [int(row[5].replace(',', '')) for row in result]

        # 创建并打印表格
        table = PrettyTable()
        table.field_names = ["ID", "Country/Area", "UN Continental Region", "UN Statistical Subregion", "Population 2022", "Population 2023", "Population Change"]

        for row in result:
            table.add_row(row)

        print(table)

        # 创建柱状图
        plt.bar(countries, population_2023)
        plt.xlabel('Country')
        plt.ylabel('Population (2023)')
        plt.title('Top 10 Countries by Population (2023)')
        plt.xticks(rotation=45)
        plt.show()

finally:
    connection.close()
