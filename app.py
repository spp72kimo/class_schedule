from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import datetime as t

# 引入 schedlue module
from schedule import schedule, find_schedule, find_kk


app = Flask(__name__)

line_bot_api = LineBotApi('RuY0urC5XyZu/m4kzz2T4Kycwiiky6qcI7ANvcDg6FWszscZsopcWL52iOdVeelgF2iGOCWqf9TnJ4RcAIW1rCWtwyNBoFj3JrdYHdkheEc1ed5YR87tpiE5r/NXraNsDOGX+6Cs/JPTTJ8aU9BhVgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('097e8b2597ec677795e676bcbab9e5a5')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    utc_time = t.datetime.now(t.timezone.utc)
    local_time = utc_time.now((t.timezone(t.timedelta(hours=8))))
    day = local_time.day
    print(day)
    msg = event.message.text

    msg_list = msg.split()
    cmd = msg_list[0]
    
    if cmd == '時間':
        reply = '遠端時間是：' + str(t.datetime.now()) + '\n' + '這裡時間是：' + str(dt2)
    elif cmd == '當日':
        reply = schedule('H2', day)
        reply += schedule('H3', day)
    elif cmd == '明天':
        reply = schedule('H2', day+1)
        reply += schedule('H3', day+1)
    elif cmd.isdigit() and int(msg) > 0 and int(msg) <= 31:
        reply = schedule('H2', int(msg))
        reply += schedule('H3', int(msg))
    elif cmd == '區間':
        min = msg_list[1]
        max = msg_list[2]
        for d in range(min,max+1):
            reply = schedule('H2', d)
            reply += schedule('H3', d)
    elif cmd == '小柯':
        result = find_schedule('H3', day)
        reply = find_kk(result)
    else:
        reply = '歡迎查詢Outlet班表\n' + '請輸入:\n1. H2\n2. H3\n3. 明天\n4. 日期(1~31)'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()