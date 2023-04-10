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



# if __name__ == '__main__':
#     app.run(debug=True)


 if __name__ == '__main__':
     app.run()  # 



#这将以非调试模式运行应用程序，避免了上述安全和兼容性问题。在本地开发环境中，您可以继续使用 debug=True 参数。为了在不同环境中使用不同设置，您可以根据需要修改代码，例如：
