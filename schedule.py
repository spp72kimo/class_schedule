from openpyxl import load_workbook
import datetime

today = datetime.date.today()						# 今天日期
day = today.day										# 今天是幾號
wb = load_workbook('202201.xlsx')					# 讀取班表Excel
sheet = wb['10011']									# 選擇工作表sheet

# 將當天上班狀況存入字典 return(dic)
def find_schedule(store=''):
	schedule = {}
	if store == 'H3':
		for row in range(8,11):
			name = sheet.cell(row, column=2)
			status = sheet.cell(row,column= day+2)
			if status.value == None:
				status = '全班'
			elif status.value == 'A':
				status = '早班'
			elif status.value == '休':
				status = '休假'
			else:
				status = status.value
			schedule[name.value] = status
	elif store == 'H2':
		for row in range(6,8):
			name = sheet.cell(row, column=2)
			status = sheet.cell(row,column= day+2)
			if status.value == None:
				status = '全班'
			elif status.value == 'A':
				status = '早班'
			elif status.value == '休':
				status = '休假'
			else:
				status = status.value
			schedule[name.value] = status
	return schedule

# 將班表結果存成字串傳回 return(str)
def show_result(store, result={}):
	#sentence = ''
	sentence = store + '今日班表：'
	sentence += str(today) + '\n'
	for r in result:
		sentence += r + ' ' + result[r] + '\n'
	return sentence
