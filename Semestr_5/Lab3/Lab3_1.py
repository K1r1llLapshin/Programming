from pathlib import Path
from skimage import io, transform, color
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-dir", required=True) # Указываем путь (обязательно) 
parser.add_argument("-augm", nargs="+", help="List: 1)rotate_90 2)rotate_45 3)resize 4)grayscale 5)complex") 

args = parser.parse_args()  
images = list(Path(args.dir).glob("*.*"))
count_file = 20

# функции преобразования изображения
def rotate_90(image): # поворот на 90 градусов
    return transform.rotate(image, 90)


def rotate_45(image):# поворот на 45 градусов
    return transform.rotate(image, 45, resize=True)


def resize(image): # изменение размера на (700, 700)
    return transform.resize(image, (700,700))


def gray_scale(image): # преобразовываем фото в градации сегого 
    return color.rgb2gray(image)


def complex_(image): # компексное преобразования (изменение размера, поворот на 45 грудусов и преобразование в градации серого)
    return gray_scale(rotate_45(resize(image)))


transform_ = { # словарь с функциями преобразования
    "rotate_90": rotate_90,
    "rotate_45": rotate_45,
    "resize": resize,
    "gray_scale": gray_scale,
    "complex": complex_,
}

for transf in args.augm:
    for image in images:
        img = io.imread(image)
        img = img[:, :, :3] # убираем альфа канал 
        new_img = transform_[transf](img) # производим преобразования
        
        new_img = (new_img * 255).astype(np.uint8) # Преобразуем изображение в формат uint8
        
        io.imsave(str(Path(args.dir) / f"{count_file}.png"), new_img)
        count_file += 1





    

