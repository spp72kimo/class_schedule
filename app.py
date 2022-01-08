from twilio.rest import Client 
from class_schedule import *
from flask import Flask

app = Flask(__name__)
@app.route("/")

def send_msg():
    account_sid = 'ACfde6f9072071bb544f06c5d38b6a8bfc' 
    auth_token = '6b2bea513a2add06478a950b29e28db3' 
    client = Client(account_sid, auth_token) 

    i = 0                # 讓訊息只發一次的開關
    hour_spec = 58       # 指定發送訊息時間
    while True:
        cur_sec = time.time()
        cur_time = time.localtime(cur_sec)
        if cur_time.tm_min == hour_spec + 1:
            i = 0
        if cur_time.tm_min == hour_spec:
            if i == 1:
                continue
            message = client.messages.create(  
                                      messaging_service_sid='MG1194dae546fa5791ccb7cd0630f86fa2', 
                                      body=sentence_h3,      
                                      to='+886938876892' 
                                  ) 
            print(message.sid)

            message = client.messages.create(  
                                      messaging_service_sid='MG1194dae546fa5791ccb7cd0630f86fa2', 
                                      body=sentence_h2,      
                                      to='+886938876892' 
                                  ) 
            print(message.sid)
            i = 1
