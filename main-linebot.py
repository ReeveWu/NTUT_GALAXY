from flask import Flask
app = Flask(__name__)

from flask import request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, QuickReply, QuickReplyButton, MessageAction, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, CarouselTemplate, CarouselColumn, PostbackTemplateAction

line_bot_api = LineBotApi('AK6iyuvwRq2hzSlpiySJbRqDa37Lny5bJhUvAB9z9TXGKs4wv6ixY84PzprtTtSVsxfui0LRbibkEaTjTPHu3p7VDr6cjnQeZtoGXG/VVCdflIoXHSsNycLmhu73k8MDlUIwmR0Mq8+oJqaAwLj0HwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ec847bcd30ff4523d230740146fb809c')

from youbike_api import ubike_search_img
from Library_go import go_Search_Library, go_Search_Library_img
from FQA import FQAList, search_ntut_club, search_ntut_club_again

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # UserId = event.source.user_id
    # profile = line_bot_api.get_profile(UserId)
    # print(profile.display_name)
    # user_id = event.source.user_id
    # print("user_id =", user_id)
    mtext = event.message.text
    if mtext == "圖書館人流":
        # line_bot_api.push_message(
        #     event.source.user_id, TextSendMessage(text='查詢中，請稍等幾秒鐘...'))
        img_link = go_Search_Library_img()
        image_message = ImageSendMessage(original_content_url=img_link,
                                         preview_image_url=img_link)
        line_bot_api.reply_message(
            event.reply_token,
            image_message)

    if mtext == "查詢附近Youbike":
        img_link = ubike_search_img()
        image_message = ImageSendMessage(original_content_url=img_link,
                                         preview_image_url=img_link)
        line_bot_api.reply_message(
            event.reply_token,
            image_message)

    elif mtext == '常見問題':
        message = FQAList()
        line_bot_api.reply_message(event.reply_token, message)

    elif mtext == "社團資訊":
        search_ntut_club(event)
    elif mtext == '【選擇】服務性社團列表':
        search_ntut_club_again(event, '服務性社團')
    elif mtext == '【選擇】體能性社團列表':
        search_ntut_club_again(event, '體能性社團')
    elif mtext == '【選擇】康樂性社團列表':
        search_ntut_club_again(event, '康樂性社團')
    elif mtext == '【選擇】音樂性社團列表':
        search_ntut_club_again(event, '音樂性社團')
    elif mtext == '【選擇】學術性社團列表':
        search_ntut_club_again(event, '學術性社團')
    elif mtext == '【選擇】聯誼性社團列表':
        search_ntut_club_again(event, '聯誼性社團')
    elif mtext == '【選擇】學生自治組織列表':
        search_ntut_club_again(event, '學生自治組織')
    elif mtext == '繼續查看其他社團':
        search_ntut_club(event)

    elif mtext == '英文畢業門檻':
        image_message = ImageSendMessage(original_content_url='https://i.imgur.com/cAosmrZ.png',
                                         preview_image_url='https://i.imgur.com/cAosmrZ.png')
        line_bot_api.reply_message(event.reply_token, image_message)

    elif mtext == '畢業學分':
        line_bot_api.reply_message(event.reply_token, TextMessage(text='小到不行'))

    elif mtext == '行事曆':
        line_bot_api.reply_message(event.reply_token, TextMessage(text='感覺人生已經到達了巔峰'))

    elif mtext == '當學期重要日程':
        line_bot_api.reply_message(event.reply_token, TextMessage(text='感覺人生已經到達了巔峰'))

    elif mtext == "校園地圖":
        image_message = ImageSendMessage(original_content_url='https://i.imgur.com/ZME2bWF.jpg',
                                         preview_image_url='https://i.imgur.com/ZME2bWF.jpg')
        line_bot_api.reply_message(event.reply_token, image_message)

    elif mtext == "FFQA":
        line_bot_api.reply_message(event.reply_token, TextMessage(text='小到不行'))

if __name__ == '__main__':
    app.run()
