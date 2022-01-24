import openpyxl
import calendar

wb = openpyxl.load_workbook('2202.xlsx')
print(wb.sheetnames)
sheet = wb['10011']

# 將原本班表底色清空
cellRange = sheet['C4':'AG10']
for row in cellRange:
	for c in row:
		c.fill = openpyxl.styles.PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type='solid')

# 將原本儲存格內資料清空
cellRange = sheet['C4':'AG10']
for row in cellRange:
	for c in row:
		c.value = ''

# 寫入月份
sheet['C2'] = '二'

# 將當月日期、星期填入儲存格
month_range = calendar.monthrange(2022, 2)
max_days = month_range[1]
weekday = month_range[0]
# print(max_days)

# 寫入當月日期
cellRange = sheet['C4':'AG4']
n = 1
for row in cellRange:
	for c in row:
		if n > max_days:
			break
		c.value = n
		n += 1

# 寫入當月星期
cellRange = sheet['C5':'AG5']
n = 1
for row in cellRange:
	for c in row:
		if n > max_days:
			break
		else:
			if weekday == 0:
				c.value = '一'
			if weekday == 1:
				c.value = '二'
			if weekday == 2:
				c.value = '三'
			if weekday == 3:
				c.value = '四'
			if weekday == 4:
				c.value = '五'
			if weekday == 5:
				c.value = '六'
			if weekday == 6:
				c.value = '日'

			n += 1	
			weekday += 1
			if weekday > 6:
				weekday = 0


# 將星期六日天數的底色轉為黃色
cellRange = sheet['C5':'AG5']
list_column = []
for row in cellRange:
	for c in row:
		if c.value == '六' or c.value == '日':
			list_column.append(c.column)

for c in list_column:
	for r in range(4, 11):
		current_cell = sheet.cell(row = r, column = c)
		current_cell.fill = openpyxl.styles.PatternFill(start_color='FFFF66', end_color='FFFF66', fill_type='solid')

# 儲存檔案
wb.save('new2202.xlsx')