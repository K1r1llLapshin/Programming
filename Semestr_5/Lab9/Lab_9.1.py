import openpyxl
from openpyxl.styles import Font, Alignment,numbers

workbook = openpyxl.Workbook()
worksheet = workbook.active

# создаем табличку, которую загрузим в Excel фаил
table_header = ['Таб. номер', 'Фамилия', 'Отдел', 'Сумма по окладу, руб.', 'Сумма по надбавкам, руб.','Сумма зарплаты, руб.', 'НДФЛ, %', 'Сумма НФДЛ, руб.', 'Сумма к выдаче, руб.']
worksheet.append(table_header)

table_person = [
    [
        {'Таб. номер': '0002', 'Фамилия': 'Петров П.П', 'Отдел': 'Бухгалтерия', 'Оклад': 3913.04, 'Надбавка': 2608.70, 'Зп': None, 'НДФЛ': 0.13, 'Сумма НДФЛ': None, 'Выдача': None},
        {'Таб. номер': '0005', 'Фамилия': 'Васин В.В', 'Отдел': 'Бухгалтерия', 'Оклад': 5934.78, 'Надбавка': 913.04, 'Зп': None, 'НДФЛ': 0.13, 'Сумма НДФЛ': None, 'Выдача': None}
    ],
    [
        {'Таб. номер': '0001', 'Фамилия': 'Иванов И.И', 'Отдел': 'Отдел кадров', 'Оклад': 6000.00, 'Надбавка': 4000.00, 'Зп': None, 'НДФЛ': 0.13, 'Сумма НДФЛ': None, 'Выдача': None},
        {'Таб. номер': '0003', 'Фамилия': 'Сидоров С.С', 'Отдел': 'Отдел кадров', 'Оклад': 5000.00, 'Надбавка': 4500.00, 'Зп': None, 'НДФЛ': 0.13, 'Сумма НДФЛ': None, 'Выдача': None},
        {'Таб. номер': '0006', 'Фамилия': 'Львов Л.Л', 'Отдел': 'Отдел кадров', 'Оклад': 4074.07, 'Надбавка': 2444.44, 'Зп': None, 'НДФЛ': 0.13, 'Сумма НДФЛ': None, 'Выдача': None},
        {'Таб. номер': '0007', 'Фамилия': 'Волков В.В', 'Отдел': 'Отдел кадров', 'Оклад': 1434.78, 'Надбавка': 1434.78, 'Зп': None, 'НДФЛ': 0.13, 'Сумма НДФЛ': None, 'Выдача': None}
    ],
    [
        {'Таб. номер': '0004', 'Фамилия': 'Мишин М.М', 'Отдел': 'Столовая', 'Оклад': 5500.00, 'Надбавка': 3500.00, 'Зп': None, 'НДФЛ': 0.13, 'Сумма НДФЛ': None, 'Выдача': None},
    ]
]

# высчитываем некотрые значения и загружаем в фаил Excel
len_B = len_C = 0
all_total_oklad = all_total_nadb = all_total_zp = all_total_sum_NDFL = all_total_out = 0

for persons in table_person:
    total_oklad = total_nadb = total_zp = total_sum_NDFL = total_out = 0
    for person in persons:
        name_otd = person['Отдел']
        len_B = len(person['Фамилия'])
        len_C = len(person['Отдел'])
        person['Зп'] = round(person['Оклад'] + person['Надбавка'], 2)
        person['Сумма НДФЛ'] = round(person['НДФЛ'] * person['Зп'], 2)
        person['Выдача'] = round(person['Зп'] - person['Сумма НДФЛ'], 2)
        
        total_oklad += person['Оклад']
        total_nadb += person['Надбавка']
        total_zp += person['Зп']
        total_sum_NDFL += person['Сумма НДФЛ']
        total_out += person['Выдача']
        
        person_list = list(person.values())
        worksheet.append(person_list)
        
    worksheet.append(['', '', name_otd + ' Итог', round(total_oklad, 2), round(total_nadb, 2), round(total_zp, 2), '', round(total_sum_NDFL, 2), round(total_out, 2)])
    
    all_total_oklad += total_oklad
    all_total_nadb += total_nadb
    all_total_zp += total_zp
    all_total_sum_NDFL += total_sum_NDFL
    all_total_out += total_out

worksheet.append(['', '', 'Общий итог', round(all_total_oklad, 2), round(all_total_nadb, 2), round(all_total_zp, 2), '', round(all_total_sum_NDFL, 2), round(all_total_out, 2)])

# Кастомизация таблички
# меняем формат ячейки и позиционирование
for char in range (ord('D'), ord('J')):
    for row in range(2,13):
        if chr(char) != 'G':
            worksheet[f'{chr(char)}{row}'].number_format = '0,00 р'
        else:  
            worksheet[f'G{row}'].number_format = numbers.FORMAT_PERCENTAGE
        worksheet[f'{chr(char)}{row}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

# делаем жирный шрифт
for i in [4,9,11,12]:
    worksheet[f'C{i}'].font = Font(bold=True)
    worksheet[f'C{i}'].alignment =  Alignment(wrap_text=True)

# поворачиваем текс и позицианируем
for char in range (ord('A'), ord('J')):
    worksheet[f'{chr(char)}1'].alignment = Alignment(text_rotation=90, horizontal='center', vertical='center', wrap_text=True)

# меняем размер колонки
worksheet.column_dimensions['B'].width = len_B * 1.5
worksheet.column_dimensions['C'].width = len_C * 1.7

workbook.save('lab9.xlsx')
