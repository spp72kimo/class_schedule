from twilio.rest import Client 
from class_schedule import *
 
account_sid = 'ACfde6f9072071bb544f06c5d38b6a8bfc' 
auth_token = '6eb26590c0ebd7e5818d0559f05746fd' 
client = Client(account_sid, auth_token) 

i = 0
hour_spec = 8
while True:
    cur_sec = time.time()
    cur_time = time.localtime(cur_sec)
    if cur_time.tm_hour == hour + 1:
        i = 0
    if cur_time.tm_hour == hour:
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
