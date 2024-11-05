from xmlschema import XMLSchema
from xml.etree import ElementTree as ET

XMLfile= ET.parse(input())
pattern = XMLSchema("./Result_5.1/pattern.xsd")

try:
    pattern.validate(XMLfile)
    print("Валидация прошла успешно")
except Exception as e:
    print(f"Ошибка валидации: {e}")

    
