
import pymysql
import matplotlib.pyplot as plt

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

        # 创建柱状图
        plt.bar(countries, population_2023)
        plt.xlabel('Country')
        plt.ylabel('Population (2023)')
        plt.title('Top 10 Countries by Population (2023)')
        plt.xticks(rotation=45)
        plt.show()

finally:
    connection.close()

# try:
#     with connection.cursor() as cursor:
#         # 查询前10行数据
#         sql = "SELECT * FROM population_data LIMIT 10;"
#         cursor.execute(sql)
#         result = cursor.fetchall()

#         # 打印查询结果
#         headers = ["id", "country_area", "un_continental_region", "un_statistical_subregion", "population_2022", "population_2023", "population_change"]
#         print(tabulate(result, headers=headers, tablefmt='grid'))
# finally:
#     connection.close()


# import pymysql
# from tabulate import tabulate

# db_host = 'localhost'
# db_user = 'root'
# db_password = '2019'
# db_name = 'population'

# connection = pymysql.connect(
#     host=db_host,
#     user=db_user,
#     password=db_password,
#     database=db_name
# )

# try:
#     with connection.cursor() as cursor:
#         # 查询前10行数据
#         sql = "SELECT * FROM population_data LIMIT 10;"
#         cursor.execute(sql)
#         result = cursor.fetchall()

#         # 打印查询结果
#         headers = ["id", "country_area", "un_continental_region", "un_statistical_subregion", "population_2022", "population_2023", "population_change"]
#         print(tabulate(result, headers=headers, tablefmt='grid'))
# finally:
#     connection.close()



# import pymysql

# db_host = 'localhost'
# db_user = 'root'
# db_password = 'your_password'
# db_name = 'population'

# connection = pymysql.connect(
#     host=db_host,
#     user=db_user,
#     password=db_password,
#     database=db_name
# )

# try:
#     with connection.cursor() as cursor:
#         # 查询前10行数据
#         sql = "SELECT * FROM population_data LIMIT 10;"
#         cursor.execute(sql)
#         result = cursor.fetchall()

#         # 打印查询结果
#         print("id, country_area, un_continental_region, un_statistical_subregion, population_2022, population_2023, population_change")
#         for row in result:
#             print(row)
# finally:
#     connection.close()
