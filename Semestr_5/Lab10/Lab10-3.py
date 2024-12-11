from docx import Document

document = Document('./Lab10/ATmega.docx')

table = document.tables[0]
ATmega328 = {}

for i in range(1,4):
    key = table.row_cells(i)[0].text
    value = table.row_cells(i)[2].text
    ATmega328[key] = value
    
print(ATmega328)