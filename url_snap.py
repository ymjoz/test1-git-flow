import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import cairosvg
import os

### 1. 通过url获取图片

# url = "https://www.cia.gov/"
# url = "https://www.u-tokyo.ac.jp/en/about/office_president.html"
# base_url = "https://www.u-tokyo.ac.jp/en/"
# base_url = "https://www.kyoto-u.ac.jp/en"
# base_url = "https://www.hokudai.ac.jp/"
base_url = "https://www.keio.ac.jp/ja/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tag = soup.find('img', )  # 需要替换为实际的图片标签和类名
if img_tag:
    image_url = img_tag['src']
    print(image_url)
    full_img_url = urljoin(base_url, image_url)
    print(full_img_url) # https://www.u-tokyo.ac.jp/content/400215559.svg

    parsed_url = urlparse(full_img_url)
    file_path = parsed_url.path
    file_name = os.path.basename(file_path)
    _, file_extension = os.path.splitext(file_name)
    
    img_name = file_name
   
    # FIXME: 如果原圖是png格式，則不需要轉換，直接保存即可 
    try:
        if file_extension == ".svg":
            cairosvg.svg2png(url=full_img_url, write_to=img_name)  # 保存图片到当前目录下
            image = Image.open(img_name)
            image.save(img_name)
        elif file_extension == ".png":
            response = requests.get(full_img_url)
            image = Image.open(BytesIO(response.content))
            image.save(img_name)
        else:
            print("Image format not supported.") 
    except:
        print("Image format unknown.") 
    
else:
    print("Image not found.")
