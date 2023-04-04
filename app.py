from flask import Flask, render_template
import pymysql
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
from prettytable import PrettyTable
import csv
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():

    # 创建数据库连接
    conn = pymysql.connect(host='choosinglove.mysql.pythonanywhere-services.com', port=3306, user='choosinglove', password='arlington2019', database='choosinglove$population')

    # 发送HTTP请求并解析网页内容
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 在Wikipedia页面中查找具有指定类名的表格
    table = soup.find("table", {"class": "wikitable"})

    with open("population.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        for row in table.select("tr"):
            row_data = []
            for cell in row.find_all(["th", "td"]):
                row_data.append(cell.text.strip())
            writer.writerow(row_data)

    with open("population.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # 跳过表头
        for row in reader:
            country_area = row[0]
            population_2023 = row[4].replace(',', '')
            sql = f"INSERT INTO population_data (country_area, population_2023) VALUES ('{country_area}', '{population_2023}')"
            with conn.cursor() as cursor:
                cursor.execute(sql)
        conn.commit()


    # 关闭数据库连接
    conn.close()

    with app.app_context():
        # 创建数据库连接
        conn = pymysql.connect(host='choosinglove.mysql.pythonanywhere-services.com', port=3306, user='choosinglove', password='arlington2019', database='choosinglove$population')

        # 读取数据
        cursor = conn.cursor()
        cursor.execute("SELECT country_area, population_2023 FROM population_data ORDER BY population_2023 DESC LIMIT 10")
        rows = cursor.fetchall()

        # 创建 PrettyTable 实例
        table = PrettyTable()
        table.field_names = ["Country", "Population (2023)"]
        for row in rows:
            print(f"Country: {row[0]}, Population: {row[1]}")
            table.add_row([row[0], row[1]])

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

if __name__ == '__main__':
    app.run(debug=True)
