import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score, mean_absolute_percentage_error
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# ================================================== ПУНКТ 1 ========================================================== #

'''
	CRIME - Уровень преступности на душу населения по городам
	HD - доля земли под жилую застройку зонирована на участки площадью более 25 000 кв. Футов.
	INDUS -  доля акров, не относящихся к розничной торговле, на город
    CHAS - Фиктивная переменная реки Чарльз (= 1, если участок ограничивает реку; 0 в противном случае)
	NOX - Концентрация оксидов азота NOX (частей на 10 миллионов)
	RM  - среднее количество комнат в доме
	AGE - ВОЗРАСТ Доля домов, построенных до 1940 года, занимаемых владельцами
	DIS - взвесила расстояния до пяти бостонских центров занятости
	RH - Индекс доступности радиальных автомобильных дорог РАД
	TAX - НАЛОГ Полная ставка налога на имущество за 10 000 долларов США
	PTRATIO - соотношение учеников и учителей по городам
	BL - B 1000 (Bk — 0,63) ^ 2, где Bk — доля чернокожего населения по городам.
	LSTAT%  - более низкий статус населения
	MEDV - Средняя стоимость частных домов в 1000 долларов
'''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score

nameColumn = ['CRIME', 'HD', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RH', 'TAX', 'PTRATIO', 'BL', 'LSTAT%', 'MEDV']

dataFrame = pd.read_csv(r"LabML_2\housing.csv", names=nameColumn, sep='\s+', engine='python')


# ================================================== Зависимость от количества данных ========================================================== #

X = dataFrame.drop(['MEDV'], axis=1) 
Y = dataFrame[['MEDV']]

sampleSizes = [0.2, 0.4, 0.6, 0.8, 1]
results1 = []

for size in sampleSizes:
    if size != 1:
        X_sub, _, Y_sub, _ = train_test_split(X, Y, train_size=size, random_state=1)
    else:
        X_sub, Y_sub = X, Y
        
    X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X_sub, Y_sub, test_size=0.3, random_state=1)
    
    model = LinearRegression()
    model.fit(X_train1, Y_train1)
    Y_pred = model.predict(X_test1)
    
    mae = mean_absolute_error(Y_test1, Y_pred)
    mape = mean_absolute_percentage_error(Y_test1, Y_pred)
    r2 = r2_score(Y_test1, Y_pred)
    
    results1.append({'SIZE': len(X_sub), 'MAE': mae, 'MAPE': mape, 'R2': r2})

print(f'{'Размер выборки':^20} | {'MAE':^10} | {"MAPE":^10} | {"R2":^10}')
print("=" * 58)
for result in results1:
    print(f"{result['SIZE']:^20} | {result['MAE']:^10.4f} | {result['MAPE']:^10.4f} | {result['R2']:^10.4f}")
    
# ================================================== Количественные переменные ========================================================== #

X4 = dataFrame[['CRIME', 'HD', 'INDUS', 'CHAS']].values
X8 = dataFrame[['CRIME', 'HD', 'INDUS', 'CHAS','RM', 'AGE', 'DIS', 'RH']].values
X12 = dataFrame[['CRIME', 'HD', 'INDUS', 'CHAS','RM', 'AGE', 'DIS', 'RH', 'TAX', 'PTRATIO', 'BL', 'LSTAT%']].values

xData = [X4, X8, X12, X]

results2 = []
for i in range(1, 5):
    X_train2, X_test2, Y_train2, Y_test2 = train_test_split(xData[i-1], Y, test_size=0.3, random_state=1)
    model = LinearRegression()
    model.fit(X_train2, Y_train2)
    Y_pred = model.predict(X_test2)
    
    mae = mean_absolute_error(Y_test2, Y_pred)
    mape = mean_absolute_percentage_error(Y_test2, Y_pred)
    r2 = r2_score(Y_test2, Y_pred)
    
    results2.append({'COUNT': i*4, 'MAE': mae, 'MAPE': mape, 'R2': r2})

print('\n')
print(f'{"Количество переменных":^20} | {"MAE":^10} | {"MAPE":^10} | {"R2":^10}')
print("=" * 58)
for result in results2:
    print(f"{result['COUNT']:^20} | {result['MAE']:^10.4f} | {result['MAPE']:^10.4f} | {result['R2']:^10.4f}")
    

# ================================================== Вывод ========================================================== #

''' 
    Cпособствует ли увеличение количества данных в датасете, улучшению точности модели и каким образом?   

При увеличении размера выборки точность модели увеличивается, что видно по увеличению значения коэффициента детерминации (R2), 
уменьшению средней абсолютной ошибки (MAE) и уменьшению средней болшой ошибки в процентах (MAPE). Это связано с тем, что большее количество 
данных позволяет обучить модель лучше и учесть больше вариаций в данных, что приводит к улучшению точности предсказаний.

При увеличении количества переменных точность модели также увеличивается, что также видно по увеличению значения коэффициента детерминации (R2),
уменьшению средней абсолютной ошибки (MAE) и уменьшению средней болшой ошибки в процентах (MAPE). Это связано с тем, что больше переменных дает 
больше информации для обучения модели и позволяет лучше учесть связи между ними, что приводит к улучшению точности предсказаний.
'''

# ================================================== ПУНКТ 2 ========================================================== #

print("\nКорреляция признаков с MEDV:")
print(dataFrame.corr()['MEDV'].sort_values(ascending=False))

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

X_vis = dataFrame[['RM', 'LSTAT%']].values
y_vis = dataFrame['MEDV'].values
model = LinearRegression()
model.fit(X_vis, y_vis)

x1 = np.linspace(X_vis[:,0].min(), X_vis[:,0].max(), 10)
x2 = np.linspace(X_vis[:,1].min(), X_vis[:,1].max(), 10)

x1_mesh, x2_mesh = np.meshgrid(x1, x2)

X_mesh = np.c_[x1_mesh.ravel(), x2_mesh.ravel()]
y_mesh = model.predict(X_mesh).reshape(x1_mesh.shape)

# Визуализация
ax.scatter(X_vis[:,0], X_vis[:,1], y_vis, c='r', marker='o', label='Реальные данные')
ax.plot_surface(x1_mesh, x2_mesh, y_mesh, alpha=0.6, cmap='viridis', label='Плоскость регрессии')
ax.set_xlabel('Среднее число комнат (RM)')
ax.set_ylabel('% населения с низким статусом (LSTAT%)')
ax.set_zlabel('Цена дома ($1000)')
ax.set_title('Зависимость цены дома от RM и LSTAT%')
plt.legend()
plt.tight_layout()
plt.show()


