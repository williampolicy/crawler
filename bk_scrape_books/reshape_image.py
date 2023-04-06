import urllib.request
from PIL import Image

image_url = "https://www.storyberries.com/wp-content/uploads/2023/03/Bedtime-stories-The-Easter-Bunny-School-short-stories-for-kids-header-978x652.jpg"
image_filename = "Bedtime-stories-The-Easter-Bunny-School-short-stories-for-kids-header-978x652.jpg"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

request = urllib.request.Request(image_url, headers=headers)
with urllib.request.urlopen(request) as url:
    with open(image_filename, "wb") as image_file:
        image_file.write(url.read())

image = Image.open(image_filename)
resized_image = image.resize((int(image.width / 10), int(image.height / 10)))
resized_image.show()




# import csv
# import os
# import urllib.request
# from PIL import Image

# # 创建本地目录用于保存图片
# if not os.path.exists('./pic'):
#     os.makedirs('./pic')

# # 读取csv文件
# with open('stories_image.csv', 'r', newline='') as file:
#     reader = csv.reader(file)
#     header = next(reader)
    
#     # 处理前5张图片
#     for i in range(5):
#         row = next(reader)
#         image_url = row[-1]
        
#         # 打开图片并进行缩小处理
#         image = Image.open(urllib.request.urlopen(image_url))
#         image.thumbnail((image.width // 10, image.height // 10))
        
#         # 保存处理后的图片到本地目录
#         filename = f"{i+1}.jpg"
#         filepath = os.path.join('./pic', filename)
#         image.save(filepath, "JPEG")
