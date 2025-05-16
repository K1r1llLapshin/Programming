from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# ========================== Иследование датасета ======================== #
iris = load_iris()
dataFrame = pd.DataFrame(iris.data, columns=iris.feature_names)
dataFrame['target'] = iris.target

sepalLength = dataFrame.iloc[:,0]
sepalWidth = dataFrame.iloc[:,1]
petalLength = dataFrame.iloc[:,2]
petalWidth = dataFrame.iloc[:,3]

plt.figure(figsize=(12,6))

# 1. График зависимости длины и ширины чашелистика
plt.subplot(1,2,1)
scatter1 = plt.scatter(sepalLength, sepalWidth, c=iris.target)
plt.scatter(sepalLength,sepalWidth,c=iris.target)
plt.title('Зависимость длины и ширины цветка')
plt.xlabel('Sepal Length (длина цветка)')
plt.ylabel('Sepal Width (ширина цветка)')
plt.legend(handles=scatter1.legend_elements()[0], labels=iris.target_names.tolist()) 

# 2. График зависимости длины и ширины лепестка
plt.subplot(1,2,2)
scatter2 = plt.scatter(petalLength, petalWidth, c=iris.target)
plt.scatter(petalLength,petalWidth,c=iris.target)
plt.title('Зависимость длины и ширины лепестков')
plt.xlabel('Petal Length (длина лепестка)')
plt.ylabel('Petal Width (ширина лепестка)')
plt.legend(handles=scatter2.legend_elements()[0], labels=iris.target_names.tolist()) 

plt.show()

# 3. Pairplot для всего датасета
sns.pairplot(dataFrame,  hue='target', palette='viridis')
plt.suptitle('Pairplot для всего набора данных Iris', y=1.02)
plt.show()

# ========================= Подготовка датасетов ========================= #

dataSet1 = dataFrame[dataFrame['target'].isin([0, 1])] # создание датасета из setosa и versicolor
dataSet2 = dataFrame[dataFrame['target'].isin([1, 2])] # создание датасета из versicolor и virginica

# ========================= Машинное обучение =========================== #
X1 = dataSet1[iris.feature_names].values
Y1 = dataSet1['target'].values

X2 = dataSet2[iris.feature_names].values
Y2 = dataSet2['target'].values

X_train1, X_test1, Y_train1, Y_test1 = train_test_split(dataSet1, Y1,test_size=0.3, random_state=0)
X_train2, X_test2, Y_train2, Y_test2 = train_test_split(dataSet2, Y2,test_size=0.3, random_state=0)

model1 = LogisticRegression(random_state=0)
model1.fit(X_train1, Y_train1)
Y_predict1 = model1.predict(X_test1)

model2 = LogisticRegression(random_state=0)
model2.fit(X_train2, Y_train2)
Y_predict2 = model2.predict(X_test2)

print('Предсказания модели для классов setosa и versicolor:', Y_predict1)
print('Предсказания модели для классов versicolor и virginica:', Y_predict2)
print('Точность предсказания для классов setosa и versicolor:', model1.score(X_test1, Y_test1))
print('Точность предсказания для классов versicolor и virginica:', model2.score(X_test2, Y_test2))

'''
Вывод программы:
    Предсказания модели для классов setosa и versicolor: [0 1 0 1 1 1 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 0 1 0 0 0 1 1 1]
    Предсказания модели для классов versicolor и virginica: [1 2 1 2 2 2 1 2 2 2 2 2 2 1 1 1 1 1 1 1 1 2 1 2 1 1 1 2 2 2]
    Точность предсказания для классов setosa и versicolor: 1.0
    Точность предсказания для классов versicolor и virginica: 1.0
'''

# ======================== Генерация датасет случайным образом ======================= #
X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, n_informative=2, random_state=1, n_clusters_per_class=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LogisticRegression(random_state=0)
model.fit(X_train, y_train)
Y_predict = model.predict(X_test)
print('\nПредсказания для случайного датасета:', Y_predict)
print('Точность предсказания для сгенерированного датасета:', model.score(X_test, y_test))

plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', alpha=0.7)
plt.title('Сгенерированный датасет')
plt.xlabel('Признак 1')
plt.ylabel('Признак 2')
plt.show()

'''
Вывод программы:
    Предсказания для случайного датасета: [1 1 0 0 1 1 1 0 1 1 1 1 1 1 1 0 1 0 1 0 0 0 1 0 1 1 1 0 1 1 1 0 1 0 1 1 0
                                           0 0 1 0 1 0 1 1 0 1 0 1 1 1 1 0 0 0 0 1 0 1 1 0 0 1 0 1 1 1 0 0 1 0 0 0 0
                                           0 1 0 0 0 0 0 1 0 1 0 1 1 0 1 1 0 0 1 1 0 0 1 1 1 1 1 0 1 0 0 0 1 0 0 1 1
                                           0 0 1 0 0 0 1 1 1 1 1 0 1 0 0 0 1 1 0 0 1 0 1 1 1 0 1 0 0 0 0 1 0 1 1 1 0
                                           0 0 0 1 0 1 0 1 1 0 0 1 0 0 0 0 0 1 1 0 1 1 0 1 1 1 1 1 0 1 0 0 1 0 1 1 0
                                           1 0 1 1 1 0 0 0 1 0 1 0 1 0 1 1 1 0 1 1 0 1 1 1 1 1 0 0 1 1 1 0 1 0 1 0 0
                                           0 0 0 1 0 1 0 0 0 1 1 1 0 0 0 0 0 0 1 0 0 1 1 1 1 1 1 0 1 1 1 1 0 0 1 0 1
                                           0 0 1 1 0 1 1 0 1 0 1 1 1 0 0 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 0 0 0 1
                                           0 1 0 0]
    Точность предсказания для сгенерированного датасета: 0.9
'''


