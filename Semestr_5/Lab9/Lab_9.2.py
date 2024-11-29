import openpyxl
from openpyxl.styles import Font, Alignment,numbers

workbook = openpyxl.load_workbook('lab9.xlsx')
worksheet = workbook.active

num_max_zp = num_min_zp = 0
max_zp = 0.0
min_zp = 99999999.0

# Вычисляем максимальное и минимальную зарплату 
for i in range(2, 11):
    if i != 4 and i != 9:
        current_value = worksheet[f'F{i}'].value
        if current_value > max_zp:
            max_zp = current_value
            num_max_zp = i
        if current_value < min_zp:
            min_zp = current_value
            num_min_zp = i 

# Вычисляем среднюю заплату по отделу
sum_buh = sum_kad = 0
for i in range(2,4):
     sum_buh += worksheet[f'F{i}'].value

for i in range(5,9):
     sum_kad += worksheet[f'F{i}'].value

data = [
    ['Максимальная зарплата', max_zp, worksheet[f'B{num_max_zp}'].value],
    ['Минимальная зарплата', min_zp, worksheet[f'B{num_min_zp}'].value],
    ['Среденя зарплата'],
    ['Бухгалтерия', sum_buh / 2],
    ['Отдел кадров', sum_kad / 4],
    ['Столовая', worksheet['F10'].value]
]

for roww in range (0, len(data)):
    for col in range(0, len(data[roww])):
        worksheet.cell(row=roww+14, column=col+2, value=data[roww][col])

# Кастомизация
worksheet['B16'].font = Font(bold=True)

for i in range(14, 21):
    worksheet[f'B{i}'].alignment = Alignment(vertical='center', wrap_text=True)
    worksheet[f'C{i}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    worksheet[f'C{i}'].number_format = '0,00 р'
    worksheet[f'D{i}'].alignment = Alignment(vertical='center', wrap_text=True)

worksheet.column_dimensions['D'].width = len(worksheet[f'B{num_min_zp}'].value) * 1.5

workbook.save('lab9.xlsx')
workbook.close()