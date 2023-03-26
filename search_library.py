import cv2
import urllib.request
import numpy as np
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def go_Search_Library():
    striing = ''
    url = 'https://lib.ntut.edu.tw/mp.asp?mp=100'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'upgrade-insecure-requests': '1',
    }

    session = HTMLSession()
    res = session.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    openTime = soup.find("div", class_="OpenTime")
    date = openTime.find('h3').text
    place = [text.text for text in openTime.find_all('a')]
    time = [text.text for text in openTime.find_all('strong')]
    isOpen = [True if text.text == '開放中' else False for text in openTime.find_all('span')[1:]]

    openTime = {}
    for index, title in enumerate(place):
        openTime[title] = {
            'time': time[index],
            'isOpen': isOpen[index]
        }
    for space in openTime:
        striing = striing + '\n位置：{}\n狀態：{}\n'.format(space,"開放中" if openTime[space]["isOpen"] else "已關閉")
        if openTime[space]["isOpen"]:
            striing = striing + '開放時間：{}\n'.format(openTime[space]["time"])
    # res.html.render(timeout=20000)
    service = []
    for i in range(4):
        soup = BeautifulSoup(res.text, "html.parser")
        info = soup.find('a', class_=f'Information0{i+1}')
        num = ''
        space = ''
        for data in list(info.text):
            if data.isdigit():
                num += data
            else:
                space += data
        if i > 0:
            url = f'https://lib.ntut.edu.tw/mp100/getSpaceCnt.asp?stype={i-1}'
            req = session.get(url)
            soup = BeautifulSoup(req.text, "html.parser")
            num = soup.find('span').text

        service.append({'space': space, 'number': int(num)})
        # service.append({'space': space, 'number': 3})
    tmp = ''
    for i in range(len(service)):
        tmp = tmp + f'{service[i]["space"]}：{service[i]["number"]}\n'
    service = tmp


    return striing, service

# a, b = go_Search_Library()
# print(a)
# print(b)
def libraryInfo_img():
    url = 'https://lib.ntut.edu.tw/mp.asp?mp=100'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'upgrade-insecure-requests': '1',
    }

    session = HTMLSession()
    res = session.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    openTime = soup.find("div", class_="OpenTime")
    place = [text.text for text in openTime.find_all('a')]
    isOpen = [True if text.text == '開放中' else False for text in openTime.find_all('span')[1:]]

    openTime = {}
    for index, title in enumerate(place):
        openTime[title] = {
            'isOpen': isOpen[index]
        }

    state_list = [True, True, True]
    state_list[0] = True if openTime['自習室']["isOpen"] else False
    state_list[1] = True if openTime['視聽室']["isOpen"] else False
    state_list[2] = True if openTime['流通櫃台']["isOpen"] else False

    url = "https://imgur.com/SZcVT0i.png"
    with urllib.request.urlopen(url) as url_response:
        img_array = np.asarray(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    url = "https://imgur.com/3SXuuO3.png"
    with urllib.request.urlopen(url) as url_response:
        img_array = np.asarray(bytearray(url_response.read()), dtype=np.uint8)
        open = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    url = "https://imgur.com/L32ojoS.png"
    with urllib.request.urlopen(url) as url_response:
        img_array = np.asarray(bytearray(url_response.read()), dtype=np.uint8)
        closed = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    xy = ((285, 620), (410, 620), (535, 620))
    for index, state in enumerate(state_list):
        x = xy[index][0]
        y = xy[index][1]
        if state:
            img[x:x + open.shape[0], y:y + open.shape[1]] = open
        else:
            img[x:x+closed.shape[0], y:y+closed.shape[1]] = closed

    service = {}
    for i in range(4):
        soup = BeautifulSoup(res.text, "html.parser")
        info = soup.find('a', class_=f'Information0{i + 1}')
        num = ''
        space = ''
        for data in list(info.text):
            if data.isdigit():
                num += data
            else:
                space += data
        if i > 0:
            url = f'https://lib.ntut.edu.tw/mp100/getSpaceCnt.asp?stype={i - 1}'
            req = session.get(url)
            soup = BeautifulSoup(req.text, "html.parser")
            num = soup.find('span').text

        service[space] = int(num)

    text_color = (192, 224, 240)
    xy = (800, 775)
    text = '{:03d}'.format(service['在館人數'])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 2.5, text_color, 4)

    text_color = (105, 79, 68)
    xy = (100, 1155)
    text = '{:03d}'.format(service['自習室席位可用席位'])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 3, text_color, 4)

    xy = (490, 1155)
    text = str(service['討論室可用數量'])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 3, text_color, 4)

    xy = (800, 1155)
    text = '{:02d}'.format(service['研究席可用席位'])
    img = cv2.putText(img, text, xy, cv2.FONT_HERSHEY_COMPLEX, 3, text_color, 4)

    from post_to_imgur import img_post
    img_link = img_post(img)

    return img_link