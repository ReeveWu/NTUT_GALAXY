import json
from flask import request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, QuickReply, QuickReplyButton, MessageAction, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, CarouselTemplate, CarouselColumn, PostbackTemplateAction, FlexSendMessage, URIAction, BubbleContainer, URITemplateAction, BoxComponent, TextComponent, ButtonComponent, ImageComponent, FlexSendMessage, BubbleContainer, CarouselContainer, CarouselColumn, TextComponent

import datetime

def recentCalendarInfo():
    with open('upcomingSchedule.json', 'r') as f:
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

def calendarSearch(mtext):
    with open('upcomingSchedule.json', 'r') as f:
        data = json.load(f)

    The_event = []
    for i in range(len(data)):
        result = datetime.date.today() < datetime.date(int(data[i]['start'][:4]), int(data[i]['start'][5:7]), int(data[i]['start'][8:10]))
        if result:
            for j in range(i, len(data)):
                if mtext in data[j]['summary']:
                    The_event.append([data[j]['summary'], data[j]['start'][:10]])
                if len(The_event) > 12:
                    break
            break
    if The_event:
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
        message = TextSendMessage(
            text="點擊下方按鈕查詢其他日程",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="查詢其他日程", text="查詢日程")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="關閉查詢", text="關閉查詢")
                    )]
            ))
        return [FlexSendMessage('profile', FlexMessage), message]
    else:
        message = TextSendMessage(
            text="查無相關日程",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="查詢其他日程", text="查詢日程")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="關閉查詢", text="關閉查詢")
                    )
                ]
            ))
        return message
print()