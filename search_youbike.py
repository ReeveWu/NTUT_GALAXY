import os
import json
import requests
from lxml import html
from bs4 import BeautifulSoup
import cv2
import urllib.request
import numpy as np
from bs4 import BeautifulSoup
from requests_html import HTMLSession

# url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
#
# dict = {}
#
# html = requests.get(url)
# dictinfo = json.loads(html.text)
# for data in dictinfo:
#     if data['sna'] in ['YouBike2.0_捷運忠孝新生站(4號出口)', 'YouBike2.0_捷運忠孝新生站(3號出口)', 'YouBike2.0_台北科技大學億光大樓', 'YouBike2.0_臺北科技大學(電機工程系)']:
#         dict[data['sna']] = [data['sbi'], data['bemp']]
#
# info = ''
# for key, value in dict.items():
#     info = info + f'\n{key}\n可借數量：{value[0]}\n可停數量：{value[1]}\n'

def ubike_search():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    html = requests.get(url)
    dictinfo = json.loads(html.text)

    dict = {}
    for data in dictinfo:
        if data['sna'] in ['YouBike2.0_捷運忠孝新生站(4號出口)', 'YouBike2.0_捷運忠孝新生站(3號出口)',
                           'YouBike2.0_台北科技大學億光大樓', 'YouBike2.0_臺北科技大學(電機工程系)']:
            dict[data['sna']] = [data['sbi'], data['bemp']]


    return dict

def ubikeInfo_img():
    dict = ubike_search()
    url = "https://imgur.com/FfPf5cJ.png"
    with urllib.request.urlopen(url) as url_response:
        img_array = np.asarray(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)


    text_color = (255, 255, 255)
    xy = (647, 293)
    text = '{:02d}'.format(dict['YouBike2.0_捷運忠孝新生站(4號出口)'][0])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 1.3, text_color, 2)

    xy = (647, 347)
    text = '{:02d}'.format(dict['YouBike2.0_捷運忠孝新生站(4號出口)'][1])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 1.3, text_color, 2)

    xy = (765, 540)
    text = '{:02d}'.format(dict['YouBike2.0_捷運忠孝新生站(3號出口)'][0])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 1.3, text_color, 2)

    xy = (765, 594)
    text = '{:02d}'.format(dict['YouBike2.0_捷運忠孝新生站(3號出口)'][1])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 1.3, text_color, 2)

    xy = (1372, 200)
    text = '{:02d}'.format(dict['YouBike2.0_臺北科技大學(電機工程系)'][0])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 1.3, text_color, 2)

    xy = (1372, 254)
    text = '{:02d}'.format(dict['YouBike2.0_臺北科技大學(電機工程系)'][1])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 1.3, text_color, 2)

    xy = (1380, 557)
    text = '{:02d}'.format(dict['YouBike2.0_台北科技大學億光大樓'][0])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 1.3, text_color, 2)

    xy = (1380, 611)
    text = '{:02d}'.format(dict['YouBike2.0_台北科技大學億光大樓'][1])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 1.3, text_color, 2)

    from post_to_imgur import img_post

    img_link = img_post(img)

    return img_link

