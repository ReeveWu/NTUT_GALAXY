from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
import os

app = Flask(__name__)

# Line Channel Access Token
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
# Line Channel Secret
CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return 'OK'
