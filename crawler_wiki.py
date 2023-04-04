import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 在Wikipedia页面中查找具有指定类名的表格
table = soup.find("table", {"class": "wikitable"})

data = []
for row in table.select("tr"):
    row_data = []
    for cell in row.find_all(["th", "td"]):
        row_data.append(cell.text.strip())
    data.append(row_data)

# 将数据保存为表格
df = pd.DataFrame(data)
df.to_csv("output_wiki.csv", index=False)
