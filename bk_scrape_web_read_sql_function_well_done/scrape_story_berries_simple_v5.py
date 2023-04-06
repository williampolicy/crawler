import requests
from bs4 import BeautifulSoup
import mysql.connector

def scrape_data():
    url = 'https://www.storyberries.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = []

    story_sections = soup.find_all('article', class_='post')

    for story_section in story_sections:
        story_title_tag = story_section.find('h2', class_='entry-title')
        story_link_tag = story_title_tag.find('a') if story_title_tag else None

        if story_link_tag:
            story_title = story_link_tag.text.strip()
            story_link = story_link_tag['href']

            # 进入详情页面获取更多信息
            story_response = requests.get(story_link)
            story_soup = BeautifulSoup(story_response.text, 'html.parser')
            author_name_tag = story_soup.find('div', class_='book-author')
            author_name = author_name_tag.text.strip() if author_name_tag else None

            stories.append({
                'title': story_title,
                'author': author_name,
                'link': story_link
            })

    return stories
