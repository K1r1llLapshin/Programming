from PIL import Image
from PIL import ImageFilter

with Image.open("C:/Users/kiril/OneDrive/Рабочий стол/DataLab2/Matroskin_2.jpg") as photo:
    photo.load()

with Image.open("C:/Users/kiril/OneDrive/Рабочий стол/DataLab2/watermark.png") as watermark:
    watermark.load()

watermark = watermark.convert('L')  # Преобразуем в grayscale
watermark = watermark.point(lambda x: 255 if x > 100 else 0)
watermark = watermark.filter(ImageFilter.CONTOUR) # Применяем фильтр контура
watermark = watermark.point(lambda x: 0 if x == 255 else 255) # Делаем watermark черно-белым
photo.paste(watermark, (300, 400), watermark)# Накладываем watermark на photo

# Отображаем изображение с watermark и сохраняем 
photo.show() 
photo.save("C:/Users/kiril/OneDrive/Рабочий стол/DataLab2/photo_with_watermark.jpg")