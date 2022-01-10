from openpyxl import load_workbook
import datetime

today = datetime.date.today()							# 今天日期
wb = load_workbook('202201.xlsx')					# 讀取班表Excel
sheet = wb['10011']									# 選擇工作表sheet

# 班表狀況格式化表示 return(str)
def represent(status):
	if status.value == None:
		status = '全班'
	elif status.value == 'A':
		status = '早班'
	elif status.value == '休':
		status = '休假'
	else:
		status = status.value
	return status

# 將當天上班狀況存入字典 return(dic)
def find_schedule(store='', day=today.day):
	schedule = {}
	if store == 'H3':
		for row in range(8,11):
			name = sheet.cell(row, column=2)
			status = sheet.cell(row,column= day+2)
			schedule[name.value] = represent(status)
	elif store == 'H2':
			for row in range(6,8):
				name = sheet.cell(row, column=2)
				status = sheet.cell(row,column= day+2)
				schedule[name.value] = represent(status)
	return schedule

# 將班表結果存成字串傳回 return(str)
def show_result(store, result={}, d=today.day):
	now = datetime.date(today.year, today.month, d)
	sentence = str(now) + '\n'
	for r in result:
		sentence += r + ' ' + result[r] + '\n'
	return sentence

#print(show_result('H3',find_schedule('H3')))