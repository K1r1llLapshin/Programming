import numpy as np

def f(x):
    return np.cos(2*x)
def df_4(x):
    return 16*np.cos(2*x)

def L_3(x):
    return 0.1333*(x**3)-1.9400*(x**2)-0.0173*x + 1.0011

def AbsoluteError(x, x_k):
    return abs(x - x_k)

def R_3(x):
    return abs((x-0.1)*(x-0.15)*(x-0.2)*(x-2.5))*(15.681/24)

x_k = [0.10, 0.15, 0.20, 0.25]
print(f"{'x_k':<10} {'y_k':<10}")
for x in x_k:
    print(f"{x:<10} {f(x):<10.4f}")

x = 0.23
fx = f(x)
L_3x = L_3(x) 
print(f'-'*40, f'\nАналитически: {fx}\nС помощью многочлена Лагранжа: {L_3x}')
print(f'Погрешность формулы Лагранжа: {R_3(x)}')
print(f'Обсалютная погрешность: {AbsoluteError(fx, L_3x)}')

