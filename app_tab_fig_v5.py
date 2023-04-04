from flask import Flask, render_template
import pymysql
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
from prettytable import PrettyTable

app = Flask(__name__)

@app.route('/')
def index():
    with app.app_context():
        # 创建数据库连接
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='2019', database='population')

        # 读取数据
        cursor = conn.cursor()
        cursor.execute("SELECT country_area, population_2023 FROM population_data ORDER BY population_2023 DESC LIMIT 10")
        rows = cursor.fetchall()

        # 3创建 PrettyTable 实例
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
