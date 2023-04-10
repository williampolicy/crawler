from flask import Flask, render_template, request
from create_bubble_chart import create_bubble_chart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    reader_input = request.form['reader_input']
    create_bubble_chart(reader_input)  # 调用bubble.py中的create_bubble_chart函数
    return render_template('result.html')



if __name__ == '__main__':
    app.run(debug=True)


