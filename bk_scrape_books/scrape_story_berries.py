import requests
from bs4 import BeautifulSoup

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
        stories.append({
            'title': story_title,
            'link': story_link
        })

print(stories)


import csv

with open('story_berries.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'link']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for story in stories:
        writer.writerow(story)
