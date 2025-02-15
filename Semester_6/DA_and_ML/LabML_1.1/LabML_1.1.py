# Линейная регресия №1 (алгоритм метода наименьших квадратов) 
import pandas as pddf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

print('Введите CSV фаил: ', end='')
file = input()

print("Поменять местами столбцы? (по умолчанию 1 столбец - x, 2 столбец - y ) y\\n: ", end='')
swap = True if input() == 'y' else False

print(swap)

