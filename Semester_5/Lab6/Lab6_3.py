import xml.etree.ElementTree as ET

XMLfile = ET.parse('./Data/ex_3.xml')
root = XMLfile.getroot()
products = root.findall('.//СведТов') 

for el in products:
    print('Наименовае товара:', el.get('НаимТов'),)
    print('\tКоличество:', el.get('КолТов'), '\n', '\tЦена:', el.get('ЦенаТов'))