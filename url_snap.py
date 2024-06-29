import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import cairosvg

### 1. 通过url获取图片

# url = "https://www.cia.gov/"
# url = "https://www.u-tokyo.ac.jp/en/about/office_president.html"
# base_url = "https://www.u-tokyo.ac.jp/en/"
# base_url = "https://www.kyoto-u.ac.jp/en"
base_url = "https://www.hokudai.ac.jp/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tag = soup.find('img', )  # 需要替换为实际的图片标签和类名
if img_tag:
    image_url = img_tag['src']
    print(image_url)
    full_img_url = urljoin(base_url, image_url)
    print(full_img_url) # https://www.u-tokyo.ac.jp/content/400215559.svg

    img_name = 'hokudai2' + '.png'
   
    # FIXME: 如果原圖是png格式，則不需要轉換，直接保存即可 
    try:
        cairosvg.svg2png(url=full_img_url, write_to=img_name)  # 保存图片到当前目录下
        image = Image.open(img_name)
        image.save(img_name)  # 保存图片到当前目录下
    except:
        print("Image png will not be converted.")
    
else:
    print("Image not found.")
