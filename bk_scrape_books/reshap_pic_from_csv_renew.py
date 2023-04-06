import csv
import urllib.request
from PIL import Image

# 读取 csv 文件
with open('stories_image.csv', 'r') as f:
    reader = csv.reader(f)
    # 跳过标题行
    next(reader)
    for row in reader:
        # 获取最后一列的图片链接
        image_url = row[-1]
        # 构造本地图片文件名
        image_filename = 'pic/' + image_url.split('/')[-1]
        try:
            # 下载图片
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
            request = urllib.request.Request(image_url, headers=headers)
            with urllib.request.urlopen(request) as url:
                with open(image_filename, "wb") as image_file:
                    image_file.write(url.read())
            # 打开并压缩图片
            image = Image.open(image_filename)
            resized_image = image.resize((int(image.width / 20), int(image.height / 20)))
            # 保存压缩后的图片
            resized_image.save(image_filename)
            # 替换 csv 文件中最后一列的数据为本地图片的路径
            row[-1] = image_filename
        except Exception as e:
            print(f"Error processing image {image_url}: {str(e)}")

# 保存修改后的 csv 文件
with open('stories_image.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'title', 'author', 'link', 'image'])
    writer.writerows(reader)
