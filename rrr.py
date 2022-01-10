import datetime
import schedule
today = datetime.date.today()
day = today.day
day += 1
print('day:',day)

result = schedule.find_schedule('H2', day)
reply1 = schedule.show_result('H2', result,13)
result = schedule.find_schedule('H3', day)
reply2 = schedule.show_result('H3', result,day)


print(reply1)
print(reply2)