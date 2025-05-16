import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score, mean_absolute_percentage_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, learning_curve
import numpy as np
import matplotlib.pyplot as plt

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

nameColumn = ['CRIME', 'HD', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RH', 'TAX', 'PTRATIO', 'BL', 'LSTAT%', 'MEDV']
dataFrame = pd.read_csv(r"LabML_4\\housing.csv", names=nameColumn, sep='\s+', engine='python')


# ======================================================= Задание 1 ======================================================= #
X = dataFrame.drop(['MEDV'], axis=1)
y = dataFrame['MEDV']

# Создание моделей линейной регрессии и KNN
linearRegressionModel = LinearRegression()
knnModel = KNeighborsRegressor()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

def drawLearningCurves (estimator, title, X, y, target_mae, cv=None):
    plt.figure(figsize=(12, 7))
    plt.title(title)   
    plt.xlabel("Размер обучающей выборки")
    plt.ylabel("Ошибка (MAE)")
    
    # Вычисление кривых обучения 
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=cv, train_sizes=np.linspace(0.1, 1.0, 20), scoring='neg_mean_absolute_error', random_state=0) 

    train_scores_mean = -np.mean(train_scores, axis=1)  # Средняя ошибка на обучении
    train_scores_std = np.std(train_scores, axis=1)     # Стандартное отклонение ошибки на обучении
    test_scores_mean = -np.mean(test_scores, axis=1)    # Средняя ошибка на валидации
    test_scores_std = np.std(test_scores, axis=1)       # Стандартное отклонение ошибки на валидации
    
    plt.grid()
    
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="b") # Область, стандартное отклонение для обучающей выборки
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color="g") # Область, стандартное отклонение для валидационной выборки
    
    plt.plot(train_sizes, train_scores_mean, 'o-', color="b", label="Ошибка на обучении")  # Линия средних значений для обучающей выборки
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Ошибка на валидации")  # Линия средних значений для валидационной выборки
    
     # Анализ с целевым значением
    plt.axhline(y=target_mae, color='r', linestyle='--', 
               label=f'Целевое MAE = {target_mae}')
    
    plt.legend(loc="best")
    plt.show()

target_mae = 3 # Целевое значение для метрики MAE 

drawLearningCurves(linearRegressionModel, "Кривая обучения (Линейная регрессия)", X_train, y_train, target_mae , cv=5)
drawLearningCurves(knnModel, "Кривая обучения (KNN регрессия)", X_train, y_train, target_mae, cv=5)

'''
Выводы:
        1. Для данного датасета больше подходит линейная регрессия.
        2. Оценка моделей:
            2.1. Линенея регрессия: 
                                   1) Кривые обучения и валидации близки друг к другу, что говорит об отсутствии переобучения.
                                   2) Ошибка (MAE) стабилизируется около 3.0–3.5.
            2.2. KNN регрессия:
                                1) Ошибка на обучении значительно меньше, чем на валидации. Это свидетельствует, что модель переобучается.
                                2) Модель не достигает целевого MAE = 3 даже на больших объемах данных.
        3. Целевое значение MAE = 3 показывает среднюю ошибку прогноза в $2500-3000. 
'''

k_values = range(1, 15)
train_errors = []
val_errors = []

# Изображаю зависимость MAE от значения k в KNN. Где к - количество соседей.
for k in k_values:
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)
    train_pred = model.predict(X_train)
    val_pred = model.predict(X_test)
    train_errors.append(mean_absolute_error(y_train, train_pred))
    val_errors.append(mean_absolute_error(y_test, val_pred))

plt.figure(figsize=(10, 6))
plt.plot(k_values, train_errors, label='Ошибка на обучении', marker='o')
plt.plot(k_values, val_errors, label='Ошибка на валидации', marker='o')
plt.axhline(y=target_mae, color='r', linestyle='--', label='Целевое MAE = 3')
plt.xlabel('Количество соседей (k)')
plt.ylabel('MAE')
plt.title('Зависимость MAE от значения k в KNN')
plt.legend()
plt.grid(True)
plt.show()

# ====================================== Задание 2 ======================================================= #

ridgeModel = Ridge(alpha=1)
lassoModel = Lasso(alpha=1)

linearRegressionModel.fit(X_train, y_train)
ridgeModel.fit(X_train, y_train)
lassoModel.fit(X_train, y_train)

linearRegression_MAE = mean_absolute_error(y_test, linearRegressionModel.predict(X_test))
ridgeModel_MAE = mean_absolute_error(y_test, ridgeModel.predict(X_test))
lassoModel_MAE = mean_absolute_error(y_test, lassoModel.predict(X_test))

linearRegression_R2 = r2_score(y_test, linearRegressionModel.predict(X_test))
ridgeModel_R2 = r2_score(y_test, ridgeModel.predict(X_test))
lassoModel_R2 = r2_score(y_test, lassoModel.predict(X_test))

linearRegression_MAPE = mean_absolute_percentage_error(y_test, linearRegressionModel.predict(X_test))
ridgeModel_MAPE = mean_absolute_percentage_error(y_test, ridgeModel.predict(X_test))
lassoModel_MAPE = mean_absolute_percentage_error(y_test, lassoModel.predict(X_test))

print(f'Линейная регрессия:\nMAE: {linearRegression_MAE:.2f}\nR2: {linearRegression_R2:.2f}\nMAPE: {linearRegression_MAPE:.2f}')
print(f'Ridge регрессия:\nMAE: {ridgeModel_MAE:.2f}\nR2: {ridgeModel_R2:.2f}\nMAPE: {ridgeModel_MAPE:.2f}')
print(f'Lasso регрессия:\nMAE: {lassoModel_MAE:.2f}\nR2: {lassoModel_R2:.2f}\nMAPE: {lassoModel_MAPE:.2f}')

weights_df = pd.DataFrame({
    "Feature": X_train.columns,
    "LinearRegression": linearRegressionModel.coef_,
    "Ridge": ridgeModel.coef_,
    "Lasso": lassoModel.coef_
})

print("\nВеса признаков:\n", weights_df)

'''
Выводы:
        1. Коллинеарность данных.
            1.1. В линейной регрессии веса некоторых признаков очень велики по модулю (например, NOX = -15.4), что может указывать на нестабильность оценок — признак коллинеарности.
            1.2. Ridge-регрессии коэффициенты уменьшаются — веса становятся ближе к нулю по модулю, особенно у NOX и INDUS.
            1.3. В Lasso-регрессии многие признаки обнуляются (например, INDUS, CHAS, NOX), что является признаком отбора признаков L1-регуляризацией. Это говорит о 
                 высокой коллинеарности этих признаков с другими.
                 
        2. Важность признаков (на основе весов).
            RM - cамый важный положительный фактор.
            LSTAT% - cамый важный отрицательный фактор.
            DIS - умеренно важный отрицательный фактор.
            PTRATIO - оттельный фактор.
            
        3. Сравнение моделей.
            3.1. Линейная регрессия: Склонна к переобучению из-за коллинеарности.
            3.2. Ridge регрессия: Устойчивее к коллинеарности, но сохраняет все признаки.
            3.3. Lasso регрессия: Упрощает модель, но теряет в точности из-за агрессивного отбора признаков.
            
            
            
Вывод программы:
    Линейная регрессия:
    MAE: 3.16
    R2: 0.71
    MAPE: 0.17
    
    Ridge регрессия:
    MAE: 3.18
    R2: 0.70
    MAPE: 0.17
    
    Lasso регрессия:
    MAE: 3.66
    R2: 0.66
    MAPE: 0.18

    Веса признаков:
        Feature  LinearRegression     Ridge     Lasso
    0     CRIME         -0.133470 -0.128427 -0.091916
    1        HD          0.035809  0.036952  0.034667
    2     INDUS          0.049523  0.017914 -0.000000
    3      CHAS          3.119835  2.932695  0.000000
    4       NOX        -15.417061 -7.848060 -0.000000
    5        RM          4.057199  4.063574  1.281317
    6       AGE         -0.010821 -0.017242  0.011440
    7       DIS         -1.385998 -1.271761 -0.616021
    8        RH          0.242727  0.225494  0.191501
    9       TAX         -0.008702 -0.009381 -0.009540
    10  PTRATIO         -0.910685 -0.827105 -0.703350
    11       BL          0.011794  0.011988  0.010832
    12   LSTAT%         -0.547113 -0.563474 -0.779921     
'''
