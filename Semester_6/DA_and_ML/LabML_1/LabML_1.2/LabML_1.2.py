from sklearn import datasets
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error, r2_score, mean_absolute_percentage_error
# ============================= Lab 1.2 ============================ #
class MyLinearRegression:
    def __init__(self):
        self.w0 = 0  
        self.w1 = 0  
        
    def fit(self, X, y):  
        n = len(X)
        sumX = np.sum(X)
        sumX_2 = np.sum(X**2)
        sumY = np.sum(y)
        sumXY = np.sum(X * y)
        self.w1 = (n * sumXY - sumX * sumY) / (n * sumX_2 - sumX**2)
        self.w0 = (sumY - self.w1 * sumX) / n
        
    def predict(self, X):
        return self.w0 + self.w1 * X

# Загрузка датасета
diabetes = datasets.load_diabetes()

# Преобразуем в DataFrame
dataFrame = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
dataFrame['target'] = diabetes.target

print('=' * 45, 'Выбираем признак', '=' * 53)
print(dataFrame.corr())
print('=' * 116)

# Видим что самая большая корреляция у 'bmi', поэтому выбираем его как признак

# Выбор признака 'bmi'
X = dataFrame['bmi'].values
Y = dataFrame['target'].values

# Разделение на обучающую и тестовую выборки
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.05)

# Преобразуем X для scikit-learn (требует 2D)
X_train_2D = X_train.reshape(-1, 1)
X_test_2D = X_test.reshape(-1, 1)

# 1. Модель scikit-learn
modelScikit = LinearRegression()
modelScikit.fit(X_train_2D, Y_train)

# 2. Моя модель
myModel = MyLinearRegression()
myModel.fit(X_train, Y_train)

# Вывод коэффициентов
print("\nКоэффициенты регрессии:")
print(f"Scikit-Learn: w1 = {modelScikit.coef_[0]:.4f}, w0 = {modelScikit.intercept_:.4f}")
print(f"Моя регрессия: w1 = {myModel.w1:.4f}, w0 = {myModel.w0:.4f}")

# Предсказания
predictionsScikit = modelScikit.predict(X_test_2D)
predictionsMyModel = myModel.predict(X_test)

yPred_my = myModel.predict(X_train)
yPred_Scikit = modelScikit.predict(X_train_2D)

# Табличный вывод сравнения
print(f'\n{"Моя регрессия":20} | {"Scikit-Learn":20} | {"Тестовые значения":20}')
for i in range(len(X_test)):
    print(f'{predictionsMyModel[i]:20.4f} | {predictionsScikit[i]:20.4f} | {Y_test[i]:20.4f}')


# ============================= Lab 1.3 ============================ #
mean_absolute_error_myModel = mean_absolute_error(Y_test, predictionsMyModel)
mean_absolute_error_Scikit = mean_absolute_error(Y_test, predictionsScikit)

mean_absolute_percentage_error_myModel = mean_absolute_percentage_error(Y_test, predictionsMyModel)
mean_absolute_percentage_error_Scikit = mean_absolute_percentage_error(Y_test, predictionsScikit)

r2_myModel = r2_score(yPred_my, Y_train)
r2_Scikit =  r2_score(yPred_Scikit, Y_train)

print(f"\nСредняя абсолютная ошибка (MAE):")
print(f"Моя модель: {mean_absolute_error_myModel:.4f}")
print(f"Scikit-Learn: {mean_absolute_error_Scikit:.4f}")

print(f"\nСредняя абсолютная ошибка в процентах (MAPE):")
print(f"Моя модель: {mean_absolute_percentage_error_myModel:.4f}")
print(f"Scikit-Learn: {mean_absolute_percentage_error_Scikit:.4f}")

print(f"\nКоэффициент детерминации (R^2):")
print(f"Моя модель: {r2_myModel:.4f}")
print(f"Scikit-Learn: {r2_Scikit:.4f}")

# ================================================================= #

predictionsScikit_graph = modelScikit.predict(X.reshape(-1, 1))
predictionsMyModel_graph = myModel.predict(X)

# отображение графиков
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X, Y, color='black', label='Фактические данные')
plt.plot(X, predictionsScikit_graph, color='blue', linewidth=3, label='Scikit-Learn')
plt.xlabel('bmi')
plt.ylabel('Target')
plt.title('Линейная регрессия (Scikit-Learn)')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(X, Y, color='black', label='Фактические данные')
plt.plot(X, predictionsMyModel_graph, color='red', linewidth=3, label='Собственная модель')
plt.xlabel('bmi')
plt.ylabel('Target')
plt.title('Линейная регрессия (Собственная реализация)')
plt.legend()

plt.tight_layout()
plt.show()

'''
Вывод программы:
    ============================================= Выбираем признак =====================================================
                age       sex       bmi        bp        s1        s2        s3        s4        s5        s6    target
    age     1.000000  0.173737  0.185085  0.335428  0.260061  0.219243 -0.075181  0.203841  0.270774  0.301731  0.187889
    sex     0.173737  1.000000  0.088161  0.241010  0.035277  0.142637 -0.379090  0.332115  0.149916  0.208133  0.043062
    bmi     0.185085  0.088161  1.000000  0.395411  0.249777  0.261170 -0.366811  0.413807  0.446157  0.388680  0.586450
    bp      0.335428  0.241010  0.395411  1.000000  0.242464  0.185548 -0.178762  0.257650  0.393480  0.390430  0.441482
    s1      0.260061  0.035277  0.249777  0.242464  1.000000  0.896663  0.051519  0.542207  0.515503  0.325717  0.212022
    s2      0.219243  0.142637  0.261170  0.185548  0.896663  1.000000 -0.196455  0.659817  0.318357  0.290600  0.174054
    s3     -0.075181 -0.379090 -0.366811 -0.178762  0.051519 -0.196455  1.000000 -0.738493 -0.398577 -0.273697 -0.394789
    s4      0.203841  0.332115  0.413807  0.257650  0.542207  0.659817 -0.738493  1.000000  0.617859  0.417212  0.430453
    s5      0.270774  0.149916  0.446157  0.393480  0.515503  0.318357 -0.398577  0.617859  1.000000  0.464669  0.565883
    s6      0.301731  0.208133  0.388680  0.390430  0.325717  0.290600 -0.273697  0.417212  0.464669  1.000000  0.382483
    target  0.187889  0.043062  0.586450  0.441482  0.212022  0.174054 -0.394789  0.430453  0.565883  0.382483  1.000000
    ====================================================================================================================

    Коэффициенты регрессии:
    Scikit-Learn: w1 = 944.4747, w0 = 151.4186
    Моя регрессия: w1 = 944.4747, w0 = 151.4186

    Моя регрессия        | Scikit-Learn         | Тестовые значения
                104.8386 |             104.8386 |             128.0000
                204.5993 |             204.5993 |             272.0000
                136.3955 |             136.3955 |              53.0000
                117.0542 |             117.0542 |             102.0000
                202.5634 |             202.5634 |             142.0000
                103.8206 |             103.8206 |              87.0000
                162.8627 |             162.8627 |             143.0000
                189.3298 |             189.3298 |             155.0000
                157.7728 |             157.7728 |             277.0000
                111.9644 |             111.9644 |             103.0000
                165.9166 |             165.9166 |             242.0000
                82.4433 |              82.4433 |             142.0000
                145.5572 |             145.5572 |             164.0000
                169.9884 |             169.9884 |             262.0000
                209.6891 |             209.6891 |             281.0000
                171.0064 |             171.0064 |             281.0000
                92.6230 |              92.6230 |              45.0000
                180.1681 |             180.1681 |             122.0000
                147.5932 |             147.5932 |              88.0000
                155.7369 |             155.7369 |             200.0000
                90.5871 |              90.5871 |             170.0000
                110.9464 |             110.9464 |              64.0000
                89.5691 |              89.5691 |              96.0000

    Средняя абсолютная ошибка (MAE):
    Моя модель: 52.9833
    Scikit-Learn: 52.9833

    Средняя абсолютная ошибка в процентах (MAPE):
    Моя модель: 0.3996
    Scikit-Learn: 0.3996

    Коэффициент детерминации (R^2):
    Моя модель: -0.9098
    Scikit-Learn: -0.9098

'''






