import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# =========================== Задание №1 ============================ #

dataFrame = pd.read_csv(r'.\\LabML_3\\Titanic.csv') # Загрузка данных из файла в датафрейм

dataFrameNew = dataFrame.dropna() # Удаление пустых значений
dataFrameNew = dataFrameNew.drop(['Name','Cabin', 'Ticket'], axis=1) # Удаление столбцов не содержащих числовые значения

lostDataPrecent = (1 - dataFrameNew.size/ dataFrame.size) * 100 # Подсчет процента потерянных данных в каждом столбце

print(f'Процент потерянных данных: {lostDataPrecent} %') # Процент потерянных данных:  84.6 %

dataFrameNew['Sex'] = dataFrameNew['Sex'].map({'male': 0, 'female': 1}) # Замена значений в столбце Sex на числовые значения
dataFrameNew['Embarked'] = dataFrameNew['Embarked'].map({'S': 1, 'C': 2, 'Q': 3}) # Замена значений в столбце Embarked на числовые значения
dataFrameNew = dataFrameNew.drop(['PassengerId'], axis=1) # Удаление столбца PassengerId, т.к. он не несёт никакой информации

# =========================== Задание №2 ============================ #
X = dataFrameNew.drop(['Survived'], axis=1) # Выделение столбцов, не являющихся ответами
y = dataFrameNew['Survived'] # Выделение столбца, содержащего ответы

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # Разделение данных на тренировочные и тестовые

model = LogisticRegression(random_state=0, max_iter=1000)

model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f'Точность модели: {score*100}')

# Оценим влияние признака Embarked на точность модели
X1 = X.drop(['Embarked'], axis=1)

model1 = LogisticRegression(random_state=0, max_iter=1000)
X_train1, X_test1, y_train1, y_test1 = train_test_split(X1, y, test_size=0.3) # Разделение данных на тренировочные и тестовые
model1.fit(X_train1, y_train1)
score = model1.score(X_test1, y_test1)
print(f'Точность модели без признака Embarked: {score*100}')

''' 
Вывод программы:
    Процент потерянных данных: 84.5959595959596 %
    Точность модели: 70.9090909090909
    Точность модели без признака Embarked: 85.45454545454545

Вывод: точности модели с признаком Embarked и без него примерно одинаковые. Из этого следует, что данный признак не влияет на результаты модели.
'''