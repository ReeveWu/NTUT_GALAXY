import os
import json
import requests
from bs4 import BeautifulSoup

studentID = '1092B0018'
url = f'https://aps.ntut.edu.tw/course/tw/Select.jsp?format=-2&code={studentID}&year=111&sem=2'
# url = f'http://nportal.ntut.edu.tw/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

cookies = {
    'JSESSIONID':'abcNF0R3fq9pU_I9qmoAy', ##
           }

html = requests.post(url, headers=headers, cookies=cookies)

week = {1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat'}
schedule = {'Mon':{}, 'Tue':{}, 'Wed':{}, 'Thu':{}, 'Fri':{}, 'Sat':{}}

soup = BeautifulSoup(html.text, "html.parser")
info = soup.find_all("tr")[:-1]
info.reverse()

for index, data in enumerate(info):
    if '班週會及導師時間' in data.text:
        info = info[:index]
        break

for index, data in enumerate(info):
    name = data.text.split('\n')[2]
    i = 0
    condition = True
    while condition:
        tmp = list(data.text.split('\n')[i+9])
        if '\u3000' not in tmp:
            i += 1
        else:
            condition = False
    for i in range(len(tmp)):
        try:
            tmp.remove(" ")
        except:
            pass
    tmp = "".join(tmp)
    tmp = tmp.split('\u3000')
    w = 1
    state = True
    classroom = tmp[-1]
    tmp = tmp[:-1]
    state_o = False
    for i in range(len(tmp)):
        try:
            if tmp[i]:
                state_o = True
            if (tmp[i] and tmp[i+1]) or (tmp[i] and state_o):
                tmp.insert(i+1, '')

        except:
            pass
    for j, detail in enumerate(tmp):
        if detail:
            state = True
            details = list(detail)
            for num, k in enumerate(details):
                if num != 0:
                    if ((ord(k) == ord(details[num - 1])+1) or ((details[num - 1]) == '9' and k == 'A') or (details[num - 1] == '4' and k == 'N')) and state:
                        schedule[week[j]][k] = name
                    elif state:
                        z = j+1
                        schedule[week[z]][k] = name
                        state = False
                    else:
                        schedule[week[z]][k] = name
                else:
                    schedule[week[j]][k] = name

file = f'.\class_schedule\{studentID}.json'
if os.path.isfile(file):
    os.remove(file)

with open(file, 'w') as f:
    json.dump(schedule, f)


print()
