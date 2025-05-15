import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import graphviz as gv

dataFrame = pd.read_csv("LabML_5/diabetes.csv")

X = dataFrame.drop(["Outcome"], axis=1)
y = dataFrame["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# ======================= Задание 1 =======================

modelLogisticReg = LogisticRegression(max_iter=1000)
modelLogisticReg.fit(X_train, y_train)
y_pred = modelLogisticReg.predict(X_test)

classification_tree = tree.DecisionTreeClassifier()
classification_tree.fit(X_train, y_train)
y_pred_tree = classification_tree.predict(X_test)

modelLogisticReg_acuracy = round(metrics.accuracy_score(y_test, y_pred), 4)
modelTree_acuracy = round(metrics.accuracy_score(y_test, y_pred_tree), 4)

modelLogisticReg_precision = round(metrics.precision_score(y_test, y_pred), 4)
modelTree_precision = round(metrics.precision_score(y_test, y_pred_tree), 4)

modelLogisticReg_f1 = round(metrics.f1_score(y_test, y_pred), 4)
modelTree_f1 = round(metrics.f1_score(y_test, y_pred_tree), 4)

print("Логистическая регрессия")
print("Accuracy: ", modelLogisticReg_acuracy)
print("Precision: ", modelLogisticReg_precision)
print("F1: ", modelLogisticReg_f1)

print("\nРешающие деревья")
print("Accuracy: ", modelTree_acuracy)
print("Precision: ", modelTree_precision)
print("F1: ", modelTree_f1)

'''
Вывод программы:
    Логистическая регрессия
    Accuracy:  0.7792
    Precision:  0.7091
    F1:  0.6047

    Решающие деревья
    Accuracy:  0.7316
    Precision:  0.5789
    F1:  0.5867

Использую метрики:
    1. Accuracy - доля правильных предсказаний среди всех случаев.
    2. Precision - точность предсказания положительного класса.
    3. F1 -балансированная мера между precision и recall.

По результатам метрик можно сделать вывод, что логистическая регрессия для данных данных лучше, чем метод решающих деревьев. 

Для следующего задания я выбираю метрику F1-score, так как:
    1. F1 обеспечивает сбалансированную оценку, особенно для несбалансированных классов.
    2. Она более информативна, чем accuracy, когда классы распределены неравномерно.               
'''
# ======================= Задание 2 =======================
depths= range(1,30)
modelTree_f1_scores = []

for depth in depths:
    modelTree = tree.DecisionTreeClassifier(max_depth=depth)
    modelTree.fit(X_train, y_train)
    y_pred_tree = modelTree.predict(X_test)
    modelTree_f1_scores.append(metrics.f1_score(y_test, y_pred_tree))

plt.figure(figsize=(10, 6))
plt.plot(depths, modelTree_f1_scores)
plt.xlabel('Глубина дерева')
plt.ylabel('F1-score')
plt.title('Зависимость F1-score от глубины дерева')
plt.show()

'''
Из графика следует, что оптимальной глубиной дерева является 5.
'''

# ======================= Задание 3 =======================

optimalModelTree = tree.DecisionTreeClassifier(max_depth=5)
optimalModelTree.fit(X_train, y_train)

dot_data = tree.export_graphviz(optimalModelTree, out_file=None)  
graph = gv.Source(dot_data)  
#graph.render("tree_graph")

# Гистограмма важности признаков
feature_importances = optimalModelTree.feature_importances_
features = X.columns

plt.figure(figsize=(12, 6))
plt.title("Важность признаков")
plt.bar(range(X.shape[1]), feature_importances, align="center")
plt.xticks(range(X.shape[1]), features, rotation=90)
plt.tight_layout()
plt.show()

metrics.PrecisionRecallDisplay.from_estimator(optimalModelTree, X_test, y_test)
plt.show()

metrics.RocCurveDisplay.from_estimator(optimalModelTree, X_test, y_test)
plt.show()

# ======================= Задание 4 =======================

max_features_range = range(1, len(X.columns)+1)
f1_scores = []

for max_features in max_features_range:
    model = tree.DecisionTreeClassifier(max_depth=5, max_features=max_features)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    f1_scores.append(metrics.f1_score(y_test, y_pred))

plt.figure(figsize=(10, 6))
plt.plot(max_features_range, f1_scores)
plt.xlabel('max_features')
plt.ylabel('F1-score')
plt.title('Зависимость оценки F1 от параметра max_features')
plt.xticks(max_features_range)
plt.grid(True)
plt.show()