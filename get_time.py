from datetime import datetime,timezone,timedelta
dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區

print('UTC \t%s\nUTC+8\t%s'%(dt1,dt2))
print(dt2.strftime("%Y-%m-%d %H:%M:%S")) # 將時間轉換為 string