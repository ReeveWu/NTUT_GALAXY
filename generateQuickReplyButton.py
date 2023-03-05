import json
from flask import Flask
from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from readJson import readClub
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, QuickReply, QuickReplyButton, MessageAction, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, CarouselTemplate, CarouselColumn, PostbackTemplateAction

def generateQuickReplyButton2(mtext, class_set):
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

    if n == 1:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        )]
            ))
        return message
    elif n == 2:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        )
                    ]
            ))
        return message
    elif n == 3:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        )
                    ]
            ))
        return message
    elif n == 4:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        )
                    ]
            ))
        return message
    elif n == 5:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[4], text=f'{mtext}\n-{class_set[4]}')
                        )
                    ]
            ))
        return message
    elif n == 6:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[4], text=f'{mtext}\n-{class_set[4]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[5], text=f'{mtext}\n-{class_set[5]}')
                        )
                    ]
            ))
        return message
    elif n == 7:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[4], text=f'{mtext}\n-{class_set[4]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[5], text=f'{mtext}\n-{class_set[5]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[6], text=f'{mtext}\n-{class_set[6]}')
                        )
                    ]
            ))
        return message
    elif n == 8:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[4], text=f'{mtext}\n-{class_set[4]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[5], text=f'{mtext}\n-{class_set[5]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[6], text=f'{mtext}\n-{class_set[6]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[7], text=f'{mtext}\n-{class_set[7]}')
                        )
                    ]
            ))
        return message
    elif n == 9:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[4], text=f'{mtext}\n-{class_set[4]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[5], text=f'{mtext}\n-{class_set[5]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[6], text=f'{mtext}\n-{class_set[6]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[7], text=f'{mtext}\n-{class_set[7]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[8], text=f'{mtext}\n-{class_set[8]}')
                        )
                    ]
            ))
        return message
    elif n == 10:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[4], text=f'{mtext}\n-{class_set[4]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[5], text=f'{mtext}\n-{class_set[5]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[6], text=f'{mtext}\n-{class_set[6]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[7], text=f'{mtext}\n-{class_set[7]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[8], text=f'{mtext}\n-{class_set[8]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[9], text=f'{mtext}\n-{class_set[9]}')
                        )
                    ]
            ))
        return message
    elif n == 11:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[4], text=f'{mtext}\n-{class_set[4]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[5], text=f'{mtext}\n-{class_set[5]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[6], text=f'{mtext}\n-{class_set[6]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[7], text=f'{mtext}\n-{class_set[7]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[8], text=f'{mtext}\n-{class_set[8]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[9], text=f'{mtext}\n-{class_set[9]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[10], text=f'{mtext}\n-{class_set[10]}')
                        )
                    ]
            ))
        return message
    elif n == 12:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[4], text=f'{mtext}\n-{class_set[4]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[5], text=f'{mtext}\n-{class_set[5]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[6], text=f'{mtext}\n-{class_set[6]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[7], text=f'{mtext}\n-{class_set[7]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[8], text=f'{mtext}\n-{class_set[8]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[9], text=f'{mtext}\n-{class_set[9]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[10], text=f'{mtext}\n-{class_set[10]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[11], text=f'{mtext}\n-{class_set[11]}')
                        )
                    ]
            ))
        return message
    elif n == 13:
        message = TextSendMessage(
                text='請選擇下方建築物',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label=class_set[0], text=f'{mtext}\n-{class_set[0]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[1], text=f'{mtext}\n-{class_set[1]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[2], text=f'{mtext}\n-{class_set[2]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[3], text=f'{mtext}\n-{class_set[3]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[4], text=f'{mtext}\n-{class_set[4]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[5], text=f'{mtext}\n-{class_set[5]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[6], text=f'{mtext}\n-{class_set[6]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[7], text=f'{mtext}\n-{class_set[7]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[8], text=f'{mtext}\n-{class_set[8]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[9], text=f'{mtext}\n-{class_set[9]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[10], text=f'{mtext}\n-{class_set[10]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[11], text=f'{mtext}\n-{class_set[11]}')
                        ),
                        QuickReplyButton(
                            action=MessageAction(label=class_set[12], text=f'{mtext}\n-{class_set[12]}')
                        )
                    ]
            ))
        return message