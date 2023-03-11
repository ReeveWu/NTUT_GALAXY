import json
from generateQuickReplyButton import generateQuickReplyButton2
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, QuickReply, QuickReplyButton, MessageAction, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, CarouselTemplate, CarouselColumn, PostbackTemplateAction

def generateQuickReplyButton(mtext, class_set):
    roomName = {'億': '億光', '化': '土木/化學/化工/設計', '共': '共同', '一': '一教', '設': '土木/化學/化工/設計',
                '先': '先鋒', '光': '光華/國百館/紡織/思源講堂', '五': '五教', '六': '六教',
                '紡': '光華/國百館/紡織/思源講堂', '三': '三教', '二': '二教', '土': '土木/化學/化工/設計',
                '科': '科研', '思': '光華/國百館/紡織/思源講堂', '國': '光華/國百館/紡織/思源講堂', '綜': '綜科',
                '四': '四教'}
    tmp = []
    class_set = list(class_set)
    for i in class_set:
        tmp.append(roomName[i])
    n = len(set(tmp))
    class_set = list(set(tmp))

    item = []
    for i in range(n):
        item.append(QuickReplyButton(
            action=MessageAction(label=class_set[i], text=f'{mtext}\n：{class_set[i]}')))

    message = TextSendMessage(
        text='請選擇下方建築物',
        quick_reply=QuickReply(
            items=item))

    return message

def searchClassroom(state, mtext):
    weekList = {'一': 'Mon', '二': 'Tue', '三': 'Wed', '四': 'Thu', '五': 'Fri'}
    if state == 0:
        week = weekList[mtext[4]]
        num = list(mtext[6:-4])
        num2 = []
        for index, number in enumerate(num):
            if number == 'N':
                num2.append(5)
            elif ord(number) >= 65 and ord(number) <= 68:
                num2.append(ord(number) - 54)
            elif int(number) >= 5 and int(number) <= 9:
                num2.append(int(number)+1)
            else:
                num2.append(int(number))

        with open('classroom.json', 'r') as f:
            data = json.load(f)
        all_class = []
        for i in num2:
            a = data[week][str(i)]
            all_class.append(a)
        if len(all_class) > 1:
            for i in range(len(all_class)):
                if i == 0:
                    a = list(set(all_class[i]) & set(all_class[i + 1]))
                elif i == len(all_class) - 1:
                    break
                else:
                    a = list(set(a) & set(all_class[i + 1]))
        class_set = []
        for i in a:
            class_set.append(i[0])
        class_set = set(class_set)
        return generateQuickReplyButton(mtext, class_set)
    else:
        week = weekList[mtext.split('\n')[0][4]]
        num = list(mtext.split('\n')[0][6:-4])
        num2 = []
        for index, number in enumerate(num):
            if number == 'N':
                num2.append(5)
            elif ord(number) >= 65 and ord(number) <= 68:
                num2.append(ord(number) - 54)
            elif int(number) >= 5 and int(number) <= 9:
                num2.append(int(number) + 1)
            else:
                num2.append(int(number))

        with open('classroom.json', 'r') as f:
            data = json.load(f)
        all_class = []
        for i in num2:
            a = data[week][str(i)]
            all_class.append(a)
        if len(all_class) > 1:
            for i in range(len(all_class)):
                if i == 0:
                    a = list(set(all_class[i]) & set(all_class[i + 1]))
                elif i == len(all_class) - 1:
                    break
                else:
                    a = list(set(a) & set(all_class[i + 1]))
        return_list = []
        mtext = mtext.split('：')[-1]
        if mtext == '土木/化學/化工/設計':
            for detail in a:
                if ('土木' in detail) or ('化學' in detail) or ('化工' in detail) or ('設計' in detail):
                    return_list.append(detail)
            return return_list
        elif mtext == '光華/國百館/紡織/思源講堂':
            for detail in a:
                if ('光華' in detail) or ('國百館' in detail) or ('紡織' in detail) or ('思源講堂' in detail):
                    return_list.append(detail)
            return return_list
        else:
            for detail in a:
                if detail[0] == mtext[0]:
                    return_list.append(detail)
            return return_list