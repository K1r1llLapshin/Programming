import openpyxl
from openpyxl.chart import PieChart, Reference

workbook = openpyxl.load_workbook('lab9.xlsx')
worksheet = workbook.active

label = Reference(worksheet, min_col= 2, min_row= 17, max_row= 19)
value = Reference(worksheet, min_col= 3, min_row= 17, max_row= 19)
pia = PieChart()

pia.add_data(value)
pia.set_categories(label)

pia.title = 'Распределение зарплаты по отделам'

worksheet.add_chart(pia,'J1')

workbook.save('lab9.xlsx')
workbook.close()
