import os
import json
import requests
from bs4 import BeautifulSoup

def readClub(clubType):
    file = f'ntutClub.json'

    with open(file, 'r') as f:
        data = json.load(f)

    datas = data[clubType]
    details = f'【{clubType}列表】\n'
    for data in datas:
        details = details + f'\n{data[0]}：\n{data[1]}\n'

    # print(data['體能性社團'][0])
    return details

# datas = readClub()
# print(type(datas))

# ---------------------------------------------------------------- #