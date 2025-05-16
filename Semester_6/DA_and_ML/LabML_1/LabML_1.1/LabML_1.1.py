# Линейная регресия №1 (алгоритм метода наименьших квадратов) 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pch

def f(x, w0, w1):
    return w0 + w1*x

def FindCoefficient(data):
    sumX, sumX_2, sumY, sumXY = 0, 0, 0, 0
    n = len(data)
    for i in range (n):
        sumX += data[i][0]
        sumX_2 += data[i][0]**2
        sumY += data[i][1]
        sumXY += data[i][1]*data[i][0]
        
    w1 = (n * sumXY - sumX*sumY)/(n * sumX_2 - sumX**2)
    w0 = (sumY - w1 * sumX)/n
    
    return w0, w1
        

print('Введите CSV фаил: ', end='')
file = input()

print("Поменять местами столбцы? (по умолчанию 1 столбец - x, 2 столбец - y ) y\\n: ", end='')
swap = True if input() == 'y' else False

data = pd.read_csv(file)
data_np = data.to_numpy()
x, y = data.columns[0], data.columns[1]

print(f"{'Название':<20}{'Количество':<20}{'Минимум':<15}{'Максимум':<15}{'Среденее':<15}")
for col in data.columns:
    print(f"{col:<20}{data[col].count():<20}{data[col].min():<15}{data[col].max():<15}{data[col].mean():<15}")

if swap:
    for i in range (len(data_np)):
        x, y = y, x
        data_np[i][0], data_np[i][1] = data_np[i][1], data_np[i][0]
        
data.plot(x=x, y=y, kind="scatter")


w0, w1 = FindCoefficient(data_np)
data_np_T = np.transpose(data_np)

plt.plot(data_np_T [0], f(data_np_T[0], w0, w1), color=(1, 0, 0))

for i in data_np:
    x = i[0]
    y = i[1]
    f_x = f(x, w0, w1)
    size = abs(f_x-y)
    rectangle = pch.Rectangle((x, min(y, f_x)), size, size, edgecolor=(1, 0.647, 0), facecolor=(1, 0.647, 0, 0.5))
    plt.subplot().add_patch(rectangle)
    
plt.show()

'''
Выводы программы:
Название            Количество          Минимум        Максимум       Среденее       
Hours               25                  1.1            9.2            5.012
Scores              25                  17             95             51.48
'''

