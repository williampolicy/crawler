import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.storyberries.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = []

# 找到所有的包含故事信息的 article 标签
story_sections = soup.find_all('article', class_='post')

# 循环遍历每个故事标签，提取标题、作者和链接
for story_section in story_sections:
    story_title_tag = story_section.find('h2', class_='entry-title')
    story_link_tag = story_title_tag.find('a') if story_title_tag else None

    if story_link_tag:
        story_title = story_link_tag.text.strip()
        story_link = story_link_tag['href']

        # 进入详情页面获取更多信息
        # story_response = requests.get(story_link)
        # story_soup = BeautifulSoup(story_response.text, 'html.parser')
        # author_name_tag = story_soup.find('div', class_='book-author')
        # author_name = author_name_tag.text.strip() if author_name_tag else None

        # 进入详情页面获取更多信息
        story_response = requests.get(story_link)
        story_soup = BeautifulSoup(story_response.text, 'html.parser')
        author_tag = story_soup.find('span', class_='author main-font vcard')
        if author_tag:
            author_name_tag = author_tag.find('a', class_='url fn n')
            author_name = author_name_tag.text.strip() if author_name_tag else None
        else:
            author_name = None

                

        stories.append({
            'title': story_title,
            'author': author_name,
            'link': story_link
        })

# 将数据保存到 CSV 文件中
with open('stories.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['title', 'author', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for story in stories:
        writer.writerow(story)
