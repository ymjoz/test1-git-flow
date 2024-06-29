import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import cairosvg
import os


def url_snapshot(base_url):
    """
    从给定的基础URL中提取图片，并将图片保存到本地的images子目录中。

    参数:
    - base_url: 字符串，表示要从中提取图片的网页的基础URL。

    返回值:
    无

    注意:
    - 该函数假设当前目录下存在名为images的子目录。
    - 如果images目录不存在，函数将不会执行图片保存操作。
    """
    # base_url = "https://www.cia.gov/"
    # url = "https://www.u-tokyo.ac.jp/en/about/office_president.html"
    # base_url = "https://www.u-tokyo.ac.jp/en/"
    # base_url = "https://www.kyoto-u.ac.jp/en"
    # base_url = "https://www.hokudai.ac.jp/"
    # base_url = "https://www.keio.ac.jp/ja/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tag = soup.find('img', )  # 需要替换为实际的图片标签和类名
    if img_tag:
        image_url = img_tag['src']
        print(image_url)
        full_img_url = urljoin(base_url, image_url)
        print(full_img_url)  # https://www.u-tokyo.ac.jp/content/400215559.svg

        parsed_url = urlparse(full_img_url)
        file_path = parsed_url.path
        file_name = os.path.basename(file_path)
        _, file_extension = os.path.splitext(file_name)

        img_name = images_path(file_name)

        # FIXME: 如果原圖是png格式，則不需要轉換，直接保存即可
        try:
            if file_extension == ".svg":
                cairosvg.svg2png(url=full_img_url,
                                 write_to=img_name)  # 保存图片到当前目录下
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


def images_path(img_name):
    # 獲取當前文件的目錄路徑
    current_dir = os.path.dirname(__file__)
    # 構建 images 子目錄的路徑
    images_dir = os.path.join(current_dir, "images")

    # 確保 images 目錄存在，如果不存在則創建它
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # 使用 os.path.join 來構建完整的文件路徑
    full_path = os.path.join(images_dir, img_name)
    return full_path


# url_snapshot("https://www.cia.gov/")
# url_snapshot("https://www.waseda.jp/top/en/")
# url_snapshot("https://www.tohoku.ac.jp/japanese/")
# url_snapshot("https://www.osaka-u.ac.jp/ja")
# url_snapshot("https://www.nagoya-u.ac.jp/")
url_snapshot("https://www.kyushu-u.ac.jp/en/")
