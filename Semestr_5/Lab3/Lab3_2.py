import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io
from sys import argv

image_path = argv[1]
with Image.open(image_path) as img:
    hist_img = img.histogram()  # Получаем гистограмму


img = io.imread(image_path)
red_hist, _ = np.histogram(img[:, :, 0], bins=256, range=[0, 256]) # Получаем гистограмму краного канала
green_hist, _ = np.histogram(img[:, :, 1], bins=256, range=[0, 256])# Получаем гистограмму зелёного канала 
blue_hist, _ = np.histogram(img[:, :, 2], bins=256, range=[0, 256])# Получаем гистограмму синего канала

# Настраиваем вывод
plt.figure(figsize=(12, 12))  # Увеличиваем размер фигуры
plt.tight_layout(pad=5.0)  # Увеличьте отступы между подграфиками
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  # Подстройка границ графиков

plt.subplot(4, 2, (1,7))
plt.imshow(img)  # Отображаем изображение
plt.axis('off')  # Скрыть оси

# Рисуем гистограмму изображения
plt.subplot(4, 2, 2)
plt.bar(range(256), hist_img[:256], color='grey', width=1)
plt.bar(range(256), hist_img[256:512], color='grey', width=1)
plt.bar(range(256), hist_img[512:], color='grey', width=1)
plt.title("Гистограмма изображения")
plt.xlabel("Яркость")
plt.ylabel("Количество пикселей")

# Рисуем гистограмму красного канала
plt.subplot(4, 2, 4)
plt.bar(range(256), red_hist, color='red', width=1)
plt.title("Красный канал")
plt.xlabel("Яркость")
plt.ylabel("Количество пикселей")

# Рисуем гистограмму зелёного канала
plt.subplot(4, 2, 6)
plt.bar(range(256), green_hist, color='green', width=1)
plt.title("Зеленый канал")
plt.xlabel("Яркость")
plt.ylabel("Количество пикселей")

# Рисуем гистограмму синего канала
plt.subplot(4, 2, 8)
plt.bar(range(256), blue_hist, color='blue', width=1)
plt.title("Синий канал")
plt.xlabel("Яркость")
plt.ylabel("Количество пикселей")

plt.tight_layout()  # Автоматически подстраиваем элементы
plt.show()