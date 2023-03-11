import json
from flask import request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, QuickReply, QuickReplyButton, MessageAction, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, CarouselTemplate, CarouselColumn, PostbackTemplateAction, FlexSendMessage, URIAction, BubbleContainer, URITemplateAction, BoxComponent, TextComponent, ButtonComponent, ImageComponent, FlexSendMessage, BubbleContainer, CarouselContainer, CarouselColumn, TextComponent

import datetime

def search_calendar():
    with open('.\\upcomingSchedule.json', 'r') as f:
        data = json.load(f)

    The_event = []
    for i in range(len(data)):
        result = datetime.date.today() < datetime.date(int(data[i]['start'][:4]), int(data[i]['start'][5:7]), int(data[i]['start'][8:10]))
        if result:
            for j in range(i, i+5):
                The_event.append([data[j]['summary'], data[j]['start'][:10]])
            break
    FlexMessage = {
        "type": "carousel",
        "contents": []
            }
    for detail in The_event:
        content = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": detail[0],
                        "color": "#000000",
                        "align": "center"
                    },
                    {
                        "type": "text",
                        "text": detail[1],
                        "align": "center"
                    }
                ],
                "backgroundColor": "#FFFFFF"
            }
        }
        FlexMessage["contents"].append(content)
    return FlexMessage
# FlexMessage = search_calendar()
print()