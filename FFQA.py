from flask import Flask
from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from readJson import readClub
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, QuickReply, QuickReplyButton, MessageAction, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, CarouselTemplate, CarouselColumn, PostbackTemplateAction

def FFQAList():
    message = TextSendMessage(
        text='看看這些有趣的問題',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(label="校園面積", text="校園面積")
                ),
                QuickReplyButton(
                    action=MessageAction(label="校史，笑死", text="校史，笑死")
                ),
                QuickReplyButton(
                    action=MessageAction(label="北科的白板是什麼顏色", text="北科的白板是什麼顏色")
                ),
                QuickReplyButton(
                    action=MessageAction(label="校歌倒過來長怎樣", text="校歌倒過來長怎樣")
                ),
                QuickReplyButton(
                    action=MessageAction(label="歷任校長", text="歷任校長")
                ),
                QuickReplyButton(
                    action=MessageAction(label="校徽", text="校徽")
                ),
                QuickReplyButton(
                    action=MessageAction(label="校訓", text="校訓")
                )
            ]
        )
    )
    return message