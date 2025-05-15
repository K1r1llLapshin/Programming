import pandas as pd
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time
import numpy as np

dataFrame = pd.read_csv("LabML_5/diabetes.csv")

X = dataFrame.drop(["Outcome"], axis=1)
y = dataFrame["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# ================= Задание №1 ==================

# ----------- исследование качества модели от глубины дерева -----------

depths = range(1, 30)
F1_scores = []

for depth in depths:
    model = RandomForestClassifier(max_depth=depth)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    F1_scores.append(f1_score(y_test, y_pred))
plt.figure(figsize=(10, 6))
plt.plot(depths, F1_scores)
plt.xticks(depths)
plt.grid()
plt.xlabel("Глубина дерева")
plt.ylabel("F1-score")
plt.title("Зависимость качества модели от глубины дерева")
plt.show()

# ----------- исследование качества модели от количества подаваемых на дерево признаков -----------
features_count = range(1, len(X.columns) + 1)
F1_scores = []
for feature in features_count:
    model = RandomForestClassifier(max_features=feature)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    F1_scores.append(f1_score(y_test, y_pred))

plt.figure(figsize=(10, 6))
plt.plot(features_count, F1_scores)
plt.xticks(features_count)
plt.grid()
plt.xlabel("Количество признаков")
plt.ylabel("F1-score")
plt.title("Зависимость качества модели от количества признаков")
plt.show()

# ----------- исследование качества модели от количества деревьев -----------

estimators_count = range(50, 80)
F1_scores = []
training_times = []
for estimator in estimators_count:
    start_time = time.time()
    model = RandomForestClassifier(n_estimators=estimator)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    F1_scores.append(f1_score(y_test, y_pred))
    training_times.append(time.time() - start_time)
    
fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:green'
ax1.set_xlabel('Количество деревьев')
ax1.set_ylabel('F1-score', color=color)
ax1.plot(estimators_count, F1_scores, marker='o', color=color, label='F1-score')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(estimators_count)
ax1.grid(True, color='gray', linestyle='--', linewidth=0.5)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Время обучения (сек)', color=color)
ax2.plot(estimators_count, training_times, marker='s', color=color, linestyle='--', label='Время обучения')
ax2.tick_params(axis='y', labelcolor=color)
ax2.grid(True, color='black', linestyle='-', linewidth=0.5)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.title('Зависимость F1-score и времени обучения от количества деревьев')
plt.tight_layout()
plt.show()

# ====================== Задание 2 =========================
from xgboost import XGBClassifier

modelBoost = XGBClassifier(reg_alpha=0.6, reg_lambda=0.3, max_depth=6, subsample=0.5, n_estimators=8)
start_time = time.time()
modelBoost.fit(X_train, y_train)
end_time = time.time() - start_time

y_pred_Boost = modelBoost.predict(X_test)

modelBoost_F1 = f1_score(y_test, y_pred_Boost)

print(modelBoost_F1, end_time)

'''
ВЫВОД:
    1. Из первого графика видно, что максимальное значение F1 достигается при глубине дерева 10 и 16. Из этого следует, что оптимальная глубина дерева равена 10.
    2. Из второго графика видно, что максимальное значение F1 достигается при количестве признаков, равном 7. Из этого следует, что оптимальное количество признаков 
       для обучения модели составляет 7.
    3. Из третьего графика видно, что скорость обучения растёт +- линейно, но при количестве деревьев 78 скорость резко упала, а F1 находится между 0.6 - 0.61. Также видно, 
       что максимальное значение F1 (~0.637) достигается при количестве деревьев 60 и скорость равна ~0.1 сек. Из этого следует, что оптимальное количество деревьев равно 60.
    
    Обучив модель с помошью библиотеки XGBoost, мы получили следующие результаты: F1 = 0.6619, время обучения = 0.05 сек. Эти результаты лучше, чем результаты, полученные
    методом случайного леса.
    
    Гиперпарвметры я подбирал последовательно путём перебора. По итогу я получил следующие наилучшие значения гиперпараметров: reg_alpha = 0.6, reg_lambda = 0.3, max_depth = 6, 
    subsample = 0.5, n_estimators = 8.
'''
