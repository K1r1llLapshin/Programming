import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, precision_score, f1_score
from sklearn.metrics import confusion_matrix, precision_recall_curve, roc_curve
import seaborn as sns
import matplotlib.pyplot as plt
# =========================== Мдель из задачи 3.2 ============================ #

dataFrame = pd.read_csv(r'.\\LabML_3\\LabML_3.2\\Titanic.csv') 

dataFrameNew = dataFrame.dropna() 
dataFrameNew = dataFrameNew.drop(['Name','Cabin', 'Ticket'], axis=1) 

lostDataPrecent = (1 - dataFrameNew.size/ dataFrame.size) * 100

print(f'Процент потерянных данных: {lostDataPrecent} %\n\n') 

dataFrameNew['Sex'] = dataFrameNew['Sex'].map({'male': 0, 'female': 1})
dataFrameNew['Embarked'] = dataFrameNew['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
dataFrameNew = dataFrameNew.drop(['PassengerId'], axis=1) 

X = dataFrameNew.drop(['Survived'], axis=1) 
y = dataFrameNew['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression(random_state=0, max_iter=1000)

model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(f'Линениная регрессия\nТочность модели: {score*100}')

# =========================================================================== #

# =================== Метрики для модели из задачаи 3.2 ===================== #

y_pred = model.predict(X_test)
y_scores = model.predict_proba(X_test)[:, 1]
recall_ = recall_score(y_test, y_pred)
precision_ = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Метрика Recall: {recall_:.2f}')
print(f'Метрика Precision: {precision_:.2f}')
print(f'Метрика F1: {f1:.2f}')

confusion = confusion_matrix(y_test, y_pred)
sns.heatmap(confusion)
plt.show()

precision, recall, _ = precision_recall_curve(y_test, y_scores)

plt.plot(precision, recall)
plt.xlabel('Precision')
plt.ylabel('Recall')
plt.title('Линейная модель')
plt.show()

fpr, tpr, _ = roc_curve(y_test, y_scores)
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Линейная модель')
plt.show()

# =========================== модели опорных векторов ====================== #
from sklearn.svm import SVC

print('\n\nМодель опорных векторов')

svm_model = SVC(kernel='linear', probability=True, random_state=0)
svm_model.fit(X_train, y_train)
svm_score = svm_model.score(X_test, y_test)
print(f'Точность модели опорных векторов: {svm_score}')

y_pred_svm = svm_model.predict(X_test)
y_scores_svm = svm_model.predict_proba(X_test)[:, 1]

recall_svm = recall_score(y_test, y_pred_svm)
precision_svm = precision_score(y_test, y_pred_svm)
f1_svm = f1_score(y_test, y_pred_svm)

print(f'Метрика Recall: {recall_svm:.2f}')
print(f'Метрика Precision: {precision_svm:.2f}')
print(f'Метрика F1: {f1_svm:.2f}')

confusion_svm = confusion_matrix(y_test, y_pred_svm)
sns.heatmap(confusion_svm)
plt.show()

precision_svm, recall_svm, _ = precision_recall_curve(y_test, y_scores_svm)
plt.plot(precision_svm, recall_svm)
plt.xlabel('Precision')
plt.ylabel('Recall')
plt.title('Модель опорных векторов')
plt.show()

fpr_svm, tpr_svm, _ = roc_curve(y_test, y_scores_svm)
plt.plot(fpr_svm, tpr_svm)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Модель опорных векторов')
plt.show()

# ============================ Модель ближайших соседей ======================== #
from sklearn.neighbors import KNeighborsClassifier

print('\n\nМодель ближайших соседей')

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

knn_score = knn_model.score(X_test, y_test)
print(f'Точность модели ближайших соседей: {knn_score}')

y_pred_knn = knn_model.predict(X_test)
y_scores_knn = knn_model.predict_proba(X_test)[:, 1]

recall_knn = recall_score(y_test, y_pred_knn)
precision_knn = precision_score(y_test, y_pred_knn)
f1_knn = f1_score(y_test, y_pred_knn)

print(f'Метрика Recall: {recall_knn:.2f}')
print(f'Метрика Precision: {precision_knn:.2f}')
print(f'Метрика F1: {f1_knn:.2f}')

confusion_knn = confusion_matrix(y_test, y_pred_knn)
sns.heatmap(confusion_knn)
plt.show()

precision_knn, recall_knn, _ = precision_recall_curve(y_test, y_scores_knn)
plt.plot(precision_knn, recall_knn)
plt.xlabel('Precision')
plt.ylabel('Recall')
plt.title('Модель ближайших соседей')
plt.show()

fpr_knn, tpr_knn, _ = roc_curve(y_test, y_scores_knn)
plt.plot(fpr_knn, tpr_knn)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Модель ближайших соседей')
plt.show()

# ============================ Вывод ======================== #

'''
Изучая метрики, мы видим, что линейная регрессия работает лучше всех по всем метрикам, а хуже всего работает метод 'ближайшие соседи'. 
'''