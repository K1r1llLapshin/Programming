import xml.etree.ElementTree as ET

XMLfile = ET.parse("./Data/ex_2.xml")
root = XMLfile.getroot()

element_1 = ET.Element('Item')
ET.SubElement(element_1, "ArtName").text = 'Сыр Чедер'
ET.SubElement(element_1, "Barcode").text = '2000000004323'
ET.SubElement(element_1, "QNT").text = '300'
ET.SubElement(element_1, 'QNTPack').text = '300'
ET.SubElement(element_1, 'Unit').text = 'шт'
ET.SubElement(element_1, 'SN1').text = '00000015'
ET.SubElement(element_1, 'SN2').text = '04.11.2024'
ET.SubElement(element_1, 'QNTRows').text = '20'

element_2 = ET.Element('Item')
ET.SubElement(element_2, "ArtName").text = 'Сыр Пармезан'
ET.SubElement(element_2, "Barcode").text = '2000000000065'
ET.SubElement(element_2, "QNT").text = '346'
ET.SubElement(element_2, 'QNTPack').text = '346'
ET.SubElement(element_2, 'Unit').text = 'шт'
ET.SubElement(element_2, 'SN1').text = '00000020'
ET.SubElement(element_2, 'SN2').text = '04.11.2024'
ET.SubElement(element_2, 'QNTRows').text = '10'

detail = root.find('Detail')
detail.append(element_1)
detail.append(element_2)
ET.indent(XMLfile, ' ')

ForSumm = detail.findall('Item')
summ = 0
summRows = 0
for el in ForSumm:
    summ += float(el.find('QNT').text.replace(',','.'))
    summRows += int(el.find('QNTRows').text)
    
summary = root.find('Summary')
summary.find('Summ').text = str(summ).replace('.',',')
summary.find('SummRows').text = str(summRows)

XMLfile.write('./Result_6.2/ex_2_new.xml', encoding="UTF-8", xml_declaration=True)
    
    

