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



# отображение графиков
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_test, Y_test, color='black', label='Фактические данные')
plt.plot(X_test, predictionsScikit, color='blue', linewidth=3, label='Scikit-Learn')
plt.xlabel('bmi')
plt.ylabel('Target')
plt.title('Линейная регрессия (Scikit-Learn)')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(X_test, Y_test, color='black', label='Фактические данные')
plt.plot(X_test, predictionsMyModel, color='red', linewidth=3, label='Собственная модель')
plt.xlabel('bmi')
plt.ylabel('Target')
plt.title('Линейная регрессия (Собственная реализация)')
plt.legend()

plt.tight_layout()
plt.show()








