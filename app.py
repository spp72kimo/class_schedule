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
import schedule


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
    dt1 = t.datetime.utcnow().replace(tzinfo=t.timezone.utc)
    dt2 = dt1.astimezone(t.timezone(t.timedelta(hours=8))) # 轉換時區 -> 東八區    
    day = dt2.day

    msg = event.message.text
    
    if '時間' in msg:
        reply = '遠端時間是：' + str(t.datetime.now()) + '\n' + '這裡時間是：' + str(dt2)
    elif 'H2' in msg:
        result = schedule.find_schedule('H2', day)
        reply = schedule.show_result('H2', result, day)
    elif 'H3' in msg:
        result = schedule.find_schedule('H3', day)
        reply = schedule.show_result('H3', result, day)
    elif '明天' in msg:
        day += 1
        result = schedule.find_schedule('H2', day)
        reply = schedule.show_result('H2', result, day)
        result = schedule.find_schedule('H3', day)
        reply += schedule.show_result('H3', result, day)
    elif '小柯' in msg:
        result = schedule.find_schedule('H3', day)
        reply = schedule.find_kk(result)
    elif int(msg) > 0 and int(msg) <= 31:
        day = int(msg)
        result = schedule.find_schedule('H2', day)
        reply = schedule.show_result('H2', result, day)
        result = schedule.find_schedule('H3', day)
        reply += schedule.show_result('H3', result, day)
    else:
        reply = '歡迎查詢Outlet班表\n' + '請輸入\'H2\'或\'H3\'或\'明天\''


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()