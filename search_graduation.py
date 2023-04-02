import json
import requests
from linebot.models import TextMessage
def graduationInfo(student_id, class_name, school):

    # student_id = '109AB0745'
    # class_name = '資財三乙'
    # school = '進修部四技'

    # student_id = '1092B0038'
    # class_name = '工程二'
    # school = '四技'

    # student_id = '1092B0038'
    # class_name = '機械二'
    # school = '進修部四技'

    url = f"https://gnehs.github.io/ntut-course-crawler-node/{student_id[:3]}/standard.json"
    html = requests.get(url)
    lst = []
    dictinfo = json.loads(html.text)
    dictinfo_copy = dictinfo.copy()
    for key, value in dictinfo_copy.items():
        if key not in ['五專', '二技', '四技', '碩士班', '博士班', '碩士在職班', '進修部四技']:
            del dictinfo[key]
    # for key, value in dictinfo.items():
    #     for k1, v1 in value.items():
    #         if class_name[:2] in k1:
    #             lst.append([key, value[k1]['credits']])
    lst = []
    lst1 = []
    for key, value in dictinfo[school].items():
        if class_name[:2] in key:
            if not key.split(class_name[:2])[0]:
                lst1.append(key)
                str = f'{key}\n\n----【{student_id[:3]}年入學】-----\n'
                for k1, v1 in value['credits'].items():
                    if v1 != '0':
                        str = str + f'\n{k1} : {v1}'
                str = TextMessage(text=str)
                lst.append(str)

    return lst, lst1