from pathlib import Path
from sys import argv
from random import choice
from PIL import Image

pictures = list(Path(argv[1]).glob('*.*'))
random_picture = choice(pictures)  
with Image.open(str(random_picture)) as img: # выбирает случайную картинку из указанной папки
    img.load()

red, green, blue = img.split() # разделяем на 3 канала 
zero_ = red.point(lambda _:0) # созаём копию красного канала с 0 значением для пикселей 
red_layer = Image.merge ("RGB", (red, zero_ , zero_ ))
green_layer = Image.merge("RGB", (zero_ , green, zero_ ))
blue_layer = Image.merge("RGB", (zero_ , zero_ , blue))

red_layer.show()
green_layer.show()
blue_layer.show()
img.show()
