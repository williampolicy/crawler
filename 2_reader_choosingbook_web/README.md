为了实现这个功能，我们需要创建一个简单的Web应用，这里我们使用Python的Flask库。首先确保您已经安装了Flask，如果没有，请运行以下命令：

bash
Copy code
pip install flask
接下来，创建以下文件和目录：

app.py：Flask应用的主要文件。
templates/：存放HTML模板的文件夹。
templates/index.html：包含输入框和提交按钮的HTML模板。
static/：存放静态文件（如生成的气泡图）的文件夹。
文件和目录结构应如下：

arduino
Copy code
.
├── app.py
├── static/
└── templates/
    └── index.html
接下来，按照以下步骤编写代码：

编写app.py文件：
python
Copy code
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
编写templates/index.html文件：
html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Sentiment Scores Bubble Chart</title>
</head>
<body>
    <h1>Book Sentiment Scores Bubble Chart</h1>
    <form method="POST" action="/">
        <label for="reader_input">Please enter your preferences:</label>
        <input type="text" id="reader_input" name="reader_input" required>
        <input type="submit" value="Submit">
    </form>
    {% if chart_file %}
    <iframe src="{{ url_for('static', filename=chart_file) }}" width="100%" height="600px" frameborder="0"></iframe>
    {% endif %}
</body>
</html>
现在，您可以运行Flask应用：

bash
Copy code
python app.py
在浏览器中打开http://127.0.0.1:5000/，您应该可以看到输入框和提交按钮。输入您的偏好并提交，页面会显示气泡图结果。

请注意，您需要将原始代码中的数据处理和气泡图生成部分添加到app.py中的index()函数中，用于处理提交的数据并生成气泡图。在这个示例中，我们假设您已经将气泡图保存为bubble_chart.html文件。

--
准备进入 Pyhtonanywhere 

太好了！祝贺您的成功。将您的应用部署到 PythonAnywhere 是一个很好的选择，它允许您轻松地将 Flask 应用部署到云端。

为了将您的应用部署到 PythonAnywhere，请按照以下步骤操作：

注册 PythonAnywhere 帐户（如果您还没有的话）并登录。
转到 Web 选项卡，然后单击 "Add a new web app"。
选择您的应用的 Python 版本，然后选择 "Flask" 作为框架。
在 "Source code" 和 "Working Directory" 设置中，您需要指定您的应用文件的路径。建议将您的代码上传到 PythonAnywhere，然后使用这些路径。
确保您的 app.py 文件中 app.run() 调用被替换为以下内容：
python
Copy code
if __name__ == '__main__':
    app.run()
在 PythonAnywhere 中安装所需的依赖项。转到 "Consoles" 选项卡，打开一个 Bash 控制台，然后运行 pip install 命令安装您的依赖项，例如：
bash
Copy code
pip3 install --user Flask pandas scikit-learn plotly
请注意，可能需要根据您的 Python 版本和应用需求调整上述命令。

返回 "Web" 选项卡，然后单击 "Reload" 按钮重新加载您的应用。
现在，您应该能够在 PythonAnywhere 分配给您的网址上访问您的应用了。

祝您在构建推荐系统方面取得成功！如果您在部署过程中遇到任何问题或需要关于如何扩展应用的建议，请随时提问。

----

跟新目录，到了一个比较简单的位置。