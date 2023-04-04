import requests
from bs4 import BeautifulSoup
import pandas as pd

# 读取本地HTML文件
with open("sample_table.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# 解析HTML
soup = BeautifulSoup(html_content, "html.parser")

# 抓取数据
data = []
for row in soup.select("table tr"):
    row_data = []
    for cell in row.find_all(["th", "td"]):
        row_data.append(cell.text)
    data.append(row_data)

# 将数据保存为表格
df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)
