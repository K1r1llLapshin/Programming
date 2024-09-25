from PIL import Image, ImageDraw, ImageFont

test_type = ImageFont.truetype('c:\WINDOWS\Fonts\SHOWG.TTF', 40) # задаём шрифт и размер
for i in range(3):
    card = Image.new('RGB',(100,100)) # создаем карточку
    cube = ImageDraw.Draw(card) # создаём объект класса для рисования
    cube.rectangle((0, 0, 100,100), fill='white', outline='blue', width=5) # рисуем белый квадрат с синей границой в 5 пискселей 
    cube.text((42,34), str(i+1), font= test_type, fill='red') # записываем текст на него 
    card.show()
    path = "./DataLab2"+"/card_"+ str(i+1) + ".png"
    card.save(path)