from sklearn.metrics import mean_absolute_error, r2_score, mean_absolute_percentage_error
# =========================================== LabML_1.2.ipynb ========================================== #
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

dataset = pd.read_csv('LabML_1/student_scores.csv')  

dataset.shape

dataset.plot(x='Hours', y='Scores', style='o') 
plt.title('Hours vs Percentage') 
plt.xlabel('Hours Studied') 
plt.ylabel('Percentage Score') 
plt.show()

X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression 
regressor = LinearRegression() 
regressor.fit(X_train, y_train)

print(regressor.intercept_)
print(regressor.coef_)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred}) 
print(df)

mean_absolute_error_reg = mean_absolute_error(y_test, y_pred)
mean_absolute_percentage_error_reg = mean_absolute_percentage_error(y_test, y_pred)
r2_score_reg = r2_score(y_test, y_pred)

print("Средняя абсолютная ошибка (MAE) регрессии:", mean_absolute_error_reg)
print("Средняя абсолютная ошибка (MAPE) регрессии:", mean_absolute_percentage_error_reg)
print("Коэффициент детерминации (R2) регрессии:", r2_score_reg)


# =========================================== для решение задания по второй части ========================================== #
# смотреть в LabML_1.2.py