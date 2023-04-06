import requests
from bs4 import BeautifulSoup

url = 'https://www.storyberries.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = []

# Get the stories from the site main content
story_sections = soup.find_all('div', class_='elementor-post')

for story_section in story_sections:
    story_title_tag = story_section.find('h3', class_='elementor-post__title')
    story_link_tag = story_title_tag.find('a') if story_title_tag else None
    story_author_tag = story_section.find('div', class_='elementor-post__author')
    
    if story_link_tag and story_author_tag:
        story_title = story_link_tag.text.strip()
        story_link = story_link_tag['href']
        story_author = story_author_tag.text.strip()
        stories.append({
            'title': story_title,
            'link': story_link,
            'author': story_author
        })

print(stories)

import csv

with open('story_berries.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'link', 'author']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for story in stories:
        writer.writerow(story)
