import requests
import base64
import numpy as np
import cv2

def img_post(image):
    # 將numpy陣列轉換為圖片格式
    # image = cv2.imread('Avater.png')
    _, img_encoded = cv2.imencode('.png', image)

    # 將圖片轉換為base64編碼的字串
    image_base64 = base64.b64encode(img_encoded).decode('utf-8')

    # 上傳圖片到imgur
    response = requests.post(
        'https://api.imgur.com/3/image',
        headers={'Authorization': 'Client-ID f200d51901898fa'},
        data={'image': image_base64}
    )

    # 解析回傳的JSON資料，取得圖片網址
    img_link = response.json()['data']['link']

    return img_link