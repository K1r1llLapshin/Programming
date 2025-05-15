import pandas as pd
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from xgboost import XGBClassifier
import time
from scipy.stats import uniform
import numpy as np

dataFrame = pd.read_csv("LabML_5/diabetes.csv")

X = dataFrame.drop(["Outcome"], axis=1)
y = dataFrame["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

modelBoost = XGBClassifier(reg_alpha=0.6, reg_lambda=0.3, max_depth=6, subsample=0.5, n_estimators=8)
start_time = time.time()
modelBoost.fit(X_train, y_train)
end_time = time.time() - start_time
y_pred_Boost = modelBoost.predict(X_test)


# ====== Задание 1:  Random Search =======

param_dist = {
    'n_estimators': np.arange(5, 100, 5),
    'max_depth': np.arange(3, 10),
    'learning_rate': uniform(0,1),
    'subsample': uniform(0,1),
    'colsample_bytree': uniform(0,1),
    'reg_alpha': uniform(0,1),
    'reg_lambda': uniform(0,1),
    'gamma': uniform(0,1)
}

model = XGBClassifier(random_state=0)

# Настройка Random Search
random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=50,  # Количество комбинаций параметров для проверки
    scoring='f1',  # Метрика для оценки
    cv=5,  # Количество фолдов для кросс-валидации
    verbose=1,
    random_state=0,
    n_jobs=-1  # Использовать все доступные ядра процессора
)

# Запуск Random Search
start_time = time.time()
random_search.fit(X_train, y_train)
end_time = time.time() - start_time

# Вывод результатов
print("Лучшие параметры:", random_search.best_params_)
print("Лучший F1-score:", random_search.best_score_)
print(f"Время выполнения: {end_time:.2f} секунд")

''' 
Вывод программы:
    Лучшие параметры: {'colsample_bytree': np.float64(0.8649332956024927), 'gamma': np.float64(0.41139672375545455), 'learning_rate': np.float64(0.13997258549320168), 
    'max_depth': np.int64(4), 'n_estimators': np.int64(50), 'reg_alpha': np.float64(0.6974287731445636), 'reg_lambda': np.float64(0.45354268267806885), 
    'subsample': np.float64(0.7220555994703479)}
    Лучший F1-score: 0.6472116119174942
    Время выполнения: 2.27 секунд
'''

# ====== Задание 2: алгоритм TPE =======

import hyperopt as hp
from hyperopt import fmin, tpe, hp, Trials, STATUS_OK

# Определение пространства поиска гиперпараметров
space = {
    'n_estimators': hp.choice('n_estimators', range(5, 100, 5)),
    'max_depth': hp.choice('max_depth', range(3, 10)),
    'learning_rate': hp.uniform('learning_rate', 0, 1.0),
    'subsample': hp.uniform('subsample', 0, 1.0),
    'colsample_bytree': hp.uniform('colsample_bytree', 0, 1.0),
    'reg_alpha': hp.uniform('reg_alpha', 0, 1),
    'reg_lambda': hp.uniform('reg_lambda', 0, 1),
    'gamma': hp.uniform('gamma', 0, 0.5)
}

# Функция для оптимизации
def objective(params):
    model = XGBClassifier(
        n_estimators=params['n_estimators'],
        max_depth=params['max_depth'],
        learning_rate=params['learning_rate'],
        subsample=params['subsample'],
        colsample_bytree=params['colsample_bytree'],
        reg_alpha=params['reg_alpha'],
        reg_lambda=params['reg_lambda'],
        gamma=params['gamma'],
        random_state=0,
        eval_metric='logloss'
    )
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = f1_score(y_test, y_pred)
    
    return {'loss': -score, 'status': STATUS_OK}

# Запуск оптимизации
trials = Trials()
start_time = time.time()

rng = np.random.default_rng(0)
best = fmin(
    fn=objective,
    space=space,
    algo=tpe.suggest,
    max_evals=50,
    trials=trials,
    rstate=rng
)
end_time = time.time() - start_time

print("Лучшие параметры:", best)
best_f1 = -trials.best_trial['result']['loss']
print(f"Лучший F1-score: {best_f1:.4f}")
print(f"Время выполнения: {end_time:.2f} секунд")

'''
Вывод программы:
    Лучшие параметры: {'colsample_bytree': np.float64(0.990866430131278), 'gamma': np.float64(0.15270470011766013), 'learning_rate': np.float64(0.49690723124357283), 
    'max_depth': np.int64(1), 'n_estimators': np.int64(10), 'reg_alpha': np.float64(0.4697103055339882), 'reg_lambda': np.float64(0.8405267116059545), 
    'subsample': np.float64(0.8550054522714187)}
    Лучший F1-score: 0.6755
    Время выполнения: 1.36 секунд
'''

'''
ВЫВОД:
    Алгоритм TPE быстрее алгоритма Random Search, и качество получилось лучше. Время выполнения алгоритма TPE составило 1.36 секунд, а для алгоритма Random Search - 2.27 секунд. 
    Полученный лучший результат F1-score для алгоритма TPE - 0.6755, что лучше, чем для алгоритма Random Search, где получился 0.6472.
'''