from sys import argv
from PIL import Image

with Image.open(argv[1]) as img:
    img.load()

img = img.convert("RGB") # Убедимся, что точно в RGB

dominant_color = {"Red": 0, "Green": 0, "Blue": 0}
for pixel in img.getdata():
    dominant_color["Red"] += pixel[0]
    dominant_color["Green"] += pixel[1]
    dominant_color["Blue"] += pixel[2]
 
max_value = max(dominant_color.values())    
for color in dominant_color:
    if dominant_color[color] == max_value:  # Сравниваем значения
        print(color)  # Выводим имя цвета