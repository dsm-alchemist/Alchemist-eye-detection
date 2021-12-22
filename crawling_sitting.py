import time
from selenium import webdriver
from urllib.request import urlretrieve
import os
from parameter import default_path

driver = webdriver.Chrome(default_path + '/chromedriver')
# gettyimages의 페이지 하나 하나 다 넣음.
url = r'gettyimages에서 가져왔습니다.'
driver.get(url)

time.sleep(1)

images = driver.find_elements_by_css_selector(".GalleryItems-module__searchContent___CYdil > div > article > a > figure > picture > img")
img_url = []

count = 485

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)

img_folder = default_path + '/data/sitting/'

if not os.path.isdir(img_folder):  # 없으면 새로 생성하는 조건문
    os.mkdir(img_folder)

for index, link in enumerate(img_url):
    #     start = link.rfind('.')
    #     end = link.rfind('&')
    #     filetype = link[start:end]
    urlretrieve(link, img_folder + f'{count}.jpg')
    count += 1

print(f"count : {count-1}")