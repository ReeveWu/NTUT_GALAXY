from flask import Flask
from flask import request
app = Flask(__name__)

from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    MessageEvent, TextMessage,
    TextSendMessage, ImageSendMessage, TemplateSendMessage, FlexSendMessage,
    QuickReply, QuickReplyButton,
    ButtonsTemplate, MessageAction, URITemplateAction, URIAction
)

line_bot_api = LineBotApi('qCdIq5FxMn9ktvMCzGllh8PVrX5yIO9xfEZwP3DOr0WP9hmNOWvZ2zIn4TVvsCmZsxfui0LRbibkEaTjTPHu3p7VDr6cjnQeZtoGXG/VVCd6Wv6kRU2RD9owZRmIGTO3j5JeFsQJDL60NSRzdun/3QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('43e6d3ced1f72c1e55a6950d94b8f238')

from userdb import get_userInfo
from FQA import FQAList, clubInfo0, clubInfo1
from FFQA import FFQAList
from search_calendar import recentCalendarInfo, calendarSearch
from search_youbike import ubikeInfo_img
from search_library import libraryInfo_img
from search_graduation import graduationInfo
from search_classroom import emptyClassroomInfo

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return 'OK'

ubike_state = False
library_state = False
calendar_state = False
graduation_state = False
standard_lst = []

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text

    global calendar_state
    if calendar_state:
        calendar_state = False
        show_cd = calendarSearch(mtext)

        line_bot_api.reply_message(event.reply_token, show_cd)

    elif mtext == "圖書館人流":
        global library_state
        library_state = True
        message = TextSendMessage(
            text='點擊按鈕開始查詢',
            quick_reply=QuickReply(
                items=[
                QuickReplyButton(
                    action=MessageAction(label="開始查詢(需幾秒鐘的時間)", text="載入圖書館人流即時資訊")
                )]
            ))
        line_bot_api.reply_message(event.reply_token, message)
    elif mtext == "載入圖書館人流即時資訊" and library_state:
        library_state = False
        img_link = libraryInfo_img()
        image_message = ImageSendMessage(original_content_url=img_link,
                                         preview_image_url=img_link)
        line_bot_api.reply_message(event.reply_token, image_message)

    elif mtext == "查詢附近Youbike":
        global ubike_state
        ubike_state = True
        message = TextSendMessage(
            text='點擊按鈕開始查詢',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="開始查詢(需幾秒鐘的時間)", text="載入Youbike即時資訊")
                    )]
                ))
        line_bot_api.reply_message(event.reply_token, message)

    elif mtext == "載入Youbike即時資訊" and ubike_state:
        ubike_state = False
        img_link = ubikeInfo_img()
        image_message = ImageSendMessage(original_content_url=img_link,
                                         preview_image_url=img_link)
        line_bot_api.reply_message(event.reply_token, image_message)

    elif mtext == '課程查詢':
        template_message = TemplateSendMessage(
            alt_text='Button Template',
            template=ButtonsTemplate(
                title='課程查詢',
                text='點擊按鈕查詢課程',
                actions=[
                    URITemplateAction(
                        label='開始查詢',
                        uri='https://liff.line.me/1660697653-qGMoojYp'
                    )]))
        line_bot_api.reply_message(event.reply_token, template_message)

    elif mtext == '解惑商店':
        message = FQAList()
        line_bot_api.reply_message(event.reply_token, message)

    elif mtext == "社團資訊":
        clubInfo0(event)
    elif mtext == '【選擇】服務性社團列表':
        clubInfo1(event, '服務性社團')
    elif mtext == '【選擇】體能性社團列表':
        clubInfo1(event, '體能性社團')
    elif mtext == '【選擇】康樂性社團列表':
        clubInfo1(event, '康樂性社團')
    elif mtext == '【選擇】音樂性社團列表':
        clubInfo1(event, '音樂性社團')
    elif mtext == '【選擇】學術性社團列表':
        clubInfo1(event, '學術性社團')
    elif mtext == '【選擇】聯誼性社團列表':
        clubInfo1(event, '聯誼性社團')
    elif mtext == '【選擇】學生自治組織列表':
        clubInfo1(event, '學生自治組織')
    elif mtext == '繼續查看其他社團':
        clubInfo0(event)

    elif mtext == '行事曆':
        message = TextSendMessage(
            text='選擇查看行事曆的方式',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="當學期重要日程", text="當學期重要日程")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="最近日程", text="最近日程")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="查詢日程", text="查詢日程")
                    )]
            ))
        line_bot_api.reply_message(event.reply_token, message)

    elif mtext == '查詢日程':
        calendar_state = True
        line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入關鍵字"))

    elif mtext == '最近日程':
        FlexMessage = recentCalendarInfo()
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile', FlexMessage))

    elif mtext == '當學期重要日程':
        image_message = ImageSendMessage(original_content_url='https://imgur.com/uv3zAia.png',
                                         preview_image_url='https://imgur.com/uv3zAia.png')
        line_bot_api.reply_message(event.reply_token, image_message)

    elif mtext == '開啟重要日程通知':
        line_bot_api.reply_message(event.reply_token, TextSendMessage('https://notify-bot.line.me/oauth/authorize?response_type=code&client_id=iQgYatSYppkaZb4uobXjxS&redirect_uri=https://01b1-2402-7500-4e6-d672-c7e-26c2-f309-5359.jp.ngrok.io&scope=notify&state=NO_STATE'))

    elif mtext == '畢業學分與英文畢業門檻':
        try:
            image_message = ImageSendMessage(original_content_url='https://i.imgur.com/cAosmrZ.png',
                                             preview_image_url='https://i.imgur.com/cAosmrZ.png')
            user_id = event.source.user_id
            userInfo = get_userInfo(user_id)
            global standard_lst
            standard_lst, lst = graduationInfo(userInfo[0], userInfo[1], userInfo[2])
            if len(lst) > 1:
                item = []
                for i in range(len(lst)):
                    item.append(QuickReplyButton(
                        action=MessageAction(label=standard_lst[i].text.split('\n')[0], text=standard_lst[i].text.split('\n')[0])))
                message = TextSendMessage(
                    text='請選擇系組',
                    quick_reply=QuickReply(
                        items=item))
                line_bot_api.reply_message(event.reply_token, message)
                global graduation_state
                graduation_state = True
            else:
                standard_lst.append(image_message)
                line_bot_api.reply_message(event.reply_token, standard_lst)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='尚未登錄個人資訊'))


    elif graduation_state and standard_lst:
        image_message = ImageSendMessage(original_content_url='https://i.imgur.com/cAosmrZ.png',
                                         preview_image_url='https://i.imgur.com/cAosmrZ.png')
        for data in standard_lst:
            if mtext in data.text:
                line_bot_api.reply_message(event.reply_token, [data, image_message])
                graduation_state = False

    elif mtext == '畢業學分':
        line_bot_api.reply_message(event.reply_token, TextMessage(text='小到不行'))

    elif mtext == "校園地圖":
        image_message = ImageSendMessage(original_content_url='https://i.imgur.com/ZME2bWF.jpg',
                                         preview_image_url='https://i.imgur.com/ZME2bWF.jpg')
        line_bot_api.reply_message(event.reply_token, image_message)

    elif mtext == "FFQA":
        message = FFQAList()
        line_bot_api.reply_message(event.reply_token, message)

    elif mtext == "校園面積":
        line_bot_api.reply_message(event.reply_token, TextMessage(text=""">>臺北市
東校區：28,044
西校區：65,514
先鋒國際研發大樓：1,969
林森校區：559
校長宿舍：451
        
>>新北市
萬里校區：1,531,802
        
>>基隆市
萬里校區：309,146
        
>>桃園市
桃園校區：1,767
        
>>總面積：1,939,252(平方公尺)"""))
    elif mtext == "校史，笑死":
        line_bot_api.reply_message(event.reply_token, TextMessage(text="""1912年 臺灣總督府於臺北廳大加蚋堡大安莊（現址）設立「民政局學務部附屬工業講習所」。\n
1914年 民政局學務部附屬工業講習所改名「臺灣總督府工業講習所」。\n
1918年 在原址增設「臺灣總督府工業學校」，專收日籍學生。\n
1919年 「台灣總督府工業講習所」改名「臺灣公立臺北工業學校」。\n
1921年 臺灣總督府工業學校改名為「臺北州立臺北第一工業學校」，仍以日籍學生為對象。原臺北工業學校更名為「臺北州立臺北第二工業學校」，以臺籍學生為對象，二者仍在同一校舍上課。\n
1923年「臺北第一工業學校」及「臺北第二工業學校」合併，改稱為「臺北州立臺北工業學校」。\n
1929年「臺北州立臺北工業學校」之專修科由三年制改為二年制。\n
1945年 戰後，臺灣省行政長官公署接辦學校，改名「臺灣省立臺北工業職業學校」。\n
1948年 改制為專科學校，校名改為「臺灣省立臺北工業專科學校」，初為五年制，招收初中畢業生。\n
1965年 增設三年制夜間部，修業4年，招收已服兵役或免服兵役之高中及高工畢業生。\n
1972年 奉教育部推行建教合作之政策，開始與公民營企業機構實施建教合作，主要項目包括代訓人才、協助進修、技術合作與材料試驗等。\n
1981年 由台灣省政府教育廳改隸教育部，更名為「國立臺北工業專科學校」。\n
1994年 改制為「國立臺北技術學院」。\n
1997年 改名「國立臺北科技大學」。\n
2016年 桃園高級農工職業學校併入該校，成為該校附屬農工，並更名為「國立臺北科技大學附屬桃園農工高級中等學校」（簡稱北科附工）。同年6月，與華夏科技大學和台北商業大學合作，在新北市中和區工專路111號學校大門口對面的圓通寺廟產土地興建學生宿舍，可容納680床，預計2018年7月啟用。\n
2018年 配合政府政策，預計與包括昔日三大工專（另二校為今虎尾科大、高雄科大）等9所學校重啟五專部，將增設「智慧自動化工程科」招收30名學生。\n
2022年 位於台北市忠孝東路上的跨領域研究大樓，進駐與麻省理工學院共同打造的都市科技實驗室（City Science Lab），也是台灣首座的都市科技實驗室，除了MIT之外，還有柏克萊加利福尼亞大學、辛辛那提大學..等，五所頂尖美國大學共同進駐的研究中心。"""))
    elif mtext == "北科的白板是什麼顏色":
        line_bot_api.reply_message(event.reply_token, TextMessage(text="根據我所搜尋到的資訊，\n國立臺北科技大學的白板可能是白色的。"))
    elif mtext == "校歌倒過來長怎樣":
        line_bot_api.reply_message(event.reply_token, TextMessage(text="榮光取爭誠精愛親，\n興肇族民樂康家國。\n躬吾在責務成務開，\n生厚用利上趕頭迎。\n靈且巧既用並腦手，\n精其求技專其欲學。\n鋒前程工子學莘莘，\n重任校吾國建業工。"))
    elif mtext == "歷任校長":
        line_bot_api.reply_message(event.reply_token, TextMessage(text="""日治時期
第一任	  隈本繁吉
第二任	  矢口玉五郎
第三任	  吉田佐次郎
第四任	  高井利五郎
第五任	  瀧波惣之進
第六任	  千千岩助太郎
第七任	  二瓶醇

戰後時期
第一任	  杜德三
第二任	  王石安
第三任	  簡卓堅
第四任	  顧柏岩
第五任	  宋希尚
第六任	  康代光
第七任	  張丹
第八任	  趙國華
第九任	  唐智
第十任	  張文雄
第十一任   張天津
第十二任   李祖添
第十三任   姚立德
第十四任   王錫福"""))
    elif mtext == "校徽":
        image_message = ImageSendMessage(original_content_url='https://imgur.com/sEG2zGY.jpg',
                                         preview_image_url='https://imgur.com/sEG2zGY.jpg')
        line_bot_api.reply_message(event.reply_token, image_message)
    elif mtext == "校訓":
        line_bot_api.reply_message(event.reply_token, TextMessage(text="誠：存誠去偽，修己善群\n樸：純潔高尚，謙敬節儉\n精：專研術業，經研求精\n勤：淬厲奮發，努力不懈"))

    elif mtext == '尋找空教室':
        template_message = TemplateSendMessage(
            alt_text='Button Template',
            template=ButtonsTemplate(
                title='查詢空教室',
                text='點擊按鈕輸入查詢時間',
                actions=[
                    URITemplateAction(
                        label='開始查詢',
                        uri='https://liff.line.me/1660697653-X5V22KBL'
                    )]))
        line_bot_api.reply_message(event.reply_token, template_message)

    elif ('查詢星期' in mtext) and ('第' in mtext) and ('節空教室' in mtext):
        if '：' not in mtext:
            message = emptyClassroomInfo(0, mtext)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            classroom_list = emptyClassroomInfo(1, mtext)
            classroom_list.sort()
            show_str = '以下是查詢範圍內的空教室：\n\n'
            for i in classroom_list:
                show_str = show_str + i + '\n'
            show_str = show_str.rstrip('\n')
            line_bot_api.reply_message(event.reply_token, [TextMessage(text=show_str),
                                                           TextMessage(text='此資訊僅做為參考，空教室亦可能供課程外租借使用，請依實際情況為主！')])

    elif mtext == '其他資訊':
        message = TextSendMessage(
            text='點擊選項查看資訊',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="更改資料", text="更改資料")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="使用手冊", text="使用手冊")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="關於我們", text="關於我們")
                    )
                ]))
        line_bot_api.reply_message(event.reply_token, message)

    elif event.message.text == '關於我們':
        line_bot_api.reply_message(event.reply_token, TextMessage(text="""我們是一個由三位成員組成的團隊，致力於創造更方便的環境，並為使用者提供更好的生活體驗。以下是我們的介紹：

☾團隊分工
李善得：主要負責LINE Bot之LIFF( LINE Front-end Framework)，以利提供空教室查詢、課程查詢等便捷功能

吳哲丞：主要負責設計主視覺與LINE Bot多數功能像是解惑商店、附近UouBike與圖書館人流。

陳永瑩：主要負責協助LINE Bot所需資訊擷取與設計行事曆、使用資訊等

☾專案連結：
https://github.com/reeve-zc/NTUT_GALAXY

☾聯絡開發者：
若於使用過程中遇到問題，可以這樣來找我們。"""))

    elif event.message.text == '使用手冊':
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='使用手冊',
                text='請點選下方按鈕',
                actions=[
                    URIAction(
                        label='開啟',
                        uri='https://drive.google.com/uc?export=download&id=1R20_vOO_CuWOSZR83GBoWLVHY4YxKqHD'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)

    elif event.message.text == '更改資料':
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                title='更改資料',
                text='請點選下方按鈕',
                actions=[
                    URIAction(
                        label='開啟',
                        uri='https://liff.line.me/1660697653-RM4QQ9L6'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)

if __name__ == '__main__':
    app.run()