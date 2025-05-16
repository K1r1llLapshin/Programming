from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
iris = load_iris()
dataFrame = pd.DataFrame(iris.data, columns=iris.feature_names)
dataFrame['target'] = iris.target

# Выделение признаков и целевой переменной
X = dataFrame[['petal length (cm)', 'petal width (cm)']].values
y = dataFrame['target'].values

# Разделение на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Обучение модели
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X_train, y_train)

# Оценка модели
y_pred = model.predict(X_test)
print(f'Предсказания модели: {y_pred}')
print(f'Точность модели: {model.score(X_test, y_test):.2f}')

'''
Вывод программы:
    Предсказания модели: [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0 0 0 1 0 0 2 1 0 0 0 2 1 1 0 0]
    Точность модели: 1.00
'''

# Визуализация
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap=plt.cm.Set1, edgecolor='k', s=50)
plt.xlabel('Длина лепестка (см)')
plt.ylabel('Ширина лепестка (см)')
plt.title('Результаты предсказания модели')
legend_labels = ['setosa', 'versicolor', 'virginica']

plt.legend(handles=scatter.legend_elements()[0], labels=legend_labels, title="Классы")
plt.show()

