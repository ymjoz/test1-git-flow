import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import cairosvg

# url = "https://www.cia.gov/"
# url = "https://www.u-tokyo.ac.jp/en/about/office_president.html"
base_url = "https://www.u-tokyo.ac.jp/en/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tag = soup.find('img', )  # 需要替换为实际的图片标签和类名
if img_tag:
    image_url = img_tag['src']
    print(image_url)
    full_img_url = urljoin(base_url, image_url)
    print(full_img_url) # https://www.u-tokyo.ac.jp/content/400215559.svg
    
    cairosvg.svg2png(url=full_img_url, write_to='u_tokyo_logo.png')  # 保存图片到当前目录下
    
    image = Image.open('u_tokyo_logo.png')
    
    image.save("u_tokyo_logo.png")  # 保存图片到当前目录下
else:
    print("Image not found.")
