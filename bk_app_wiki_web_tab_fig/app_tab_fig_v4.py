from flask import Flask, render_template
import pymysql
import csv
from prettytable import PrettyTable
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # 爬取人口数据并保存到 CSV 文件和 MySQL 数据库的逻辑
    # ...

    # I. 从 MySQL 数据库中读取数据并展示的逻辑
    # 1创建数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='2019', database='population')
    # 2读取数据
    cursor = conn.cursor()
    cursor.execute("SELECT country_area, population_2023 FROM population_data ORDER BY population_2023 DESC LIMIT 10")
    rows = cursor.fetchall()

    # 3创建 PrettyTable 实例
    table = PrettyTable()
    table.field_names = ["Country", "Population (2023)"]
    for row in rows:
        print(f"Country: {row[0]}, Population: {row[1]}")
        table.add_row([row[0], row[1]])

    # 关闭数据库连接
    cursor.close()
    conn.close()
    # ...


    # 从 CSV 文件中读取数据并创建表格
    #table = create_table()
    #img = create_bar_chart()
    #img_base64 = base64.b64encode(img.getvalue()).decode('ascii')  # 需要做格式转换
    
    # II. fig
    # 创建数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='2019', database='population')

    # 读取数据
    cursor = conn.cursor()
    cursor.execute("SELECT country_area, population_2023 FROM population_data ORDER BY population_2023 DESC LIMIT 10")
    rows = cursor.fetchall()

    # 绘制柱状图
    countries = [row[0] for row in rows]
    population_2023 = [int(row[1].replace(',', '')) for row in rows]

    fig = plt.figure()
    plt.bar(countries, population_2023)
    plt.xlabel("Countries")
    plt.ylabel("Population (2023)")
    plt.xticks(rotation=45)

    # 将绘制好的图像以二进制数据的形式嵌入到 HTML 模板中
    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    img_data = base64.b64encode(img.getvalue()).decode('ascii')

    # 关闭数据库连接
    cursor.close()
    conn.close()

    return render_template('index.html', table=table.get_html_string(), img_data=img_data)

    #return render_template('index.html', table=table.get_html_string(), table_mysql=table_mysql.get_html_string(), img_data=img_base64)
    #return render_template('index.html', table=table.get_html_string(), img_data=img_base64)

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def create_table():
    data = []
    with open('output_wiki.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

    data.pop(0)  # 删除表头行

    filtered_data = [row for row in data[:10] if is_int(row[4].replace(',', ''))]

    # 创建 PrettyTable 实例
    table = PrettyTable()
    table.field_names = ["Country", "Population (2023)"]
    for row in filtered_data:
        table.add_row([row[0], row[4]])

    return table

def create_bar_chart():
    with open('output_wiki.csv', 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    data.pop(0)  # 删除表头行
    # 测试展示
    # for row in data:
    #     category = row[0]
    #     value = row[4]
    #     print(f"{category}: {value}")

    def is_int(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    filtered_data = [row for row in data if is_int(row[4].replace(',', ''))]
    sorted_data = sorted(filtered_data, key=lambda x: int(x[4].replace(',', '')), reverse=True)[:10]

    countries = [row[0] for row in sorted_data]
    population_2023 = [int(row[4].replace(',', '')) for row in sorted_data]

    fig = plt.figure()
    plt.bar(countries, population_2023)
    plt.xlabel("Countries")
    plt.ylabel("Population (2023)")
    plt.xticks(rotation=45)

    img = BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    return img


if __name__ == '__main__':
    app.run(debug=True)
