from flask import Flask, render_template, request
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        reader_input = request.form['reader_input']

        # 这里添加您的数据处理和气泡图生成代码
        # 假设最后生成的气泡图已经保存为 bubble_chart.html 文件

        return render_template('index.html', chart_file='bubble_chart.html')
    return render_template('index.html', chart_file=None)

if __name__ == '__main__':
    app.run(debug=True)
