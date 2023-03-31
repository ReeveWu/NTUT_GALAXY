from flask import Flask
from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from readJson import readClub
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, QuickReply, QuickReplyButton, MessageAction, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, CarouselTemplate, CarouselColumn, PostbackTemplateAction

line_bot_api = LineBotApi('qCdIq5FxMn9ktvMCzGllh8PVrX5yIO9xfEZwP3DOr0WP9hmNOWvZ2zIn4TVvsCmZsxfui0LRbibkEaTjTPHu3p7VDr6cjnQeZtoGXG/VVCd6Wv6kRU2RD9owZRmIGTO3j5JeFsQJDL60NSRzdun/3QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('43e6d3ced1f72c1e55a6950d94b8f238')

def FQAList():
    message = TextSendMessage(
        text='選擇下方常見問題',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="畢業學分與英文畢業門檻", text="畢業學分與英文畢業門檻")
                ),
                QuickReplyButton(
                    action=MessageAction(label="社團資訊", text="社團資訊")
                ),
                QuickReplyButton(
                    action=MessageAction(label="行事曆", text="行事曆")
                ),
                QuickReplyButton(
                    action=MessageAction(label="校園地圖", text="校園地圖")
                ),
                QuickReplyButton(
                    action=MessageAction(label="FFQA", text="FFQA")
                )
            ]
        )
    )
    return message

def clubInfo0(event):  #轉盤樣板
    message = TemplateSendMessage(
        alt_text='社團查詢',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='服務性社團',
                    text=' 點擊【選擇】查看此類型社團',
                    actions=[
                        MessageTemplateAction(
                                    label='選擇',
                                    text='【選擇】服務性社團列表'
                                    ),
                    ]
                ),
                CarouselColumn(
                    title='體能性社團',
                    text=' 點擊【選擇】查看此類型社團',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='【選擇】體能性社團列表'
                            ),
                    ]
                ),
                CarouselColumn(
                    title='聯誼性社團',
                    text=' 點擊【選擇】查看此類型社團',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='【選擇】聯誼性社團列表'
                            ),
                    ]
                ),
                CarouselColumn(
                    title='音樂性社團',
                    text=' 點擊【選擇】查看此類型社團',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='【選擇】音樂性社團列表'
                            ),
                    ]
                ),
                CarouselColumn(
                    title='學術性社團',
                    text=' 點擊【選擇】查看此類型社團',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='【選擇】學術性社團列表'
                            ),
                    ]
                ),
                CarouselColumn(
                    title='學生自治組織',
                    text=' 點擊【選擇】查看此類型社團',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='【選擇】學生自治組織列表'
                            ),
                    ]
                ),
                CarouselColumn(
                    title='康樂性社團',
                    text=' 點擊【選擇】查看此類型社團',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='【選擇】康樂性社團列表'
                            ),
                    ]
                ),
            ])
        )
    line_bot_api.reply_message(event.reply_token,message)

def clubInfo1(event, name):
    data = readClub(name)
    message = TextSendMessage(
                text=data,
                quick_reply=QuickReply(
                items=[QuickReplyButton(action=MessageAction(label='繼續查看其他社團', text='繼續查看其他社團')
                        ),
                       QuickReplyButton(action=MessageAction(label='結束查詢', text='結束查詢')
                                        )
                    ]
                )
            )
    line_bot_api.reply_message(event.reply_token, message)