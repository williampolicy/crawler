from flask import Flask, render_template
import pymysql
import csv
from prettytable import PrettyTable
# import matplotlib.pyplot as plt
# from io import BytesIO
# import base64


app = Flask(__name__)

@app.route('/')
def index():
    # 爬取人口数据并保存到 CSV 文件和 MySQL 数据库的逻辑
    # ...

    # 从 MySQL 数据库中读取数据并展示的逻辑
    # ...

    # 从 CSV 文件中读取数据并创建表格
    table = create_table()

    return render_template('index.html', table=table.get_html_string())
    # img_data=img_base64 改动后无需 img_data 变量


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def create_table():
    with open('output_wiki.csv', 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    data.pop(0)  # 删除表头行

    filtered_data = [row for row in data[:10] if is_int(row[5].replace(',', ''))]
    
    # 创建 PrettyTable 实例
    table = PrettyTable()
    table.field_names = ["Country", "Population (2023)"]
    for row in filtered_data:
        table.add_row([row[1], row[5]])

    return table

# 注释掉创建图表的相关函数
# def create_bar_chart():
# ...


if __name__ == '__main__':
    app.run(debug=True)
