import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*np.sin(2*x) - x**2

def derivative_f(x):
    return -4*np.cos(2*x)+2*x

accuracy = 10**-7

def Newton_method(x):
    iterations = 1
    y = x - f(x)/derivative_f(x)
    print(f'{y}')
    while (abs(y - x) > accuracy):
        iterations += 1
        x = y
        y = y - f(y)/derivative_f(y)
        print(f'{y:}')
    print('iterations: ', iterations)

def Chord_method(x, c):
    iterations = 1
    y = x - f(x)/(f(c) - f(x)) * (c - x)
    print(f'{y}')
    while (abs(y - x) > accuracy):
        iterations += 1
        x = y
        y = y - f(y)/(f(c) - f(y)) * (c - y)
        print(f'{y:}')
    print('iterations: ', iterations)

def Secant_method(x, y):
    iterations = 0
    while (abs(y - x) > accuracy):
        iterations += 1
        z = x
        x = y
        y = x - f(x)/(f(x) - f(z)) * (x - z)
        print(f'{y:}')
    print('iterations: ', iterations)

def Newton_method_two(x, h):
    iterations = 1
    y = x - h*f(x)/(f(x + h) - f(x))
    print(f'{y}')
    while (abs(y - x) > accuracy):
        iterations += 1
        x = y
        y = x - h*f(x)/(f(x + h) - f(x))
        print(f'{y:}')
    print('iterations: ', iterations)
    
def Steffensens_method(x):
    iterations = 0
    while True:
        y = x - f(x)**2 / (f(x + f(x)) - f(x))
        iterations += 1
        print(f'{y}')
        
        if abs(y - x) <= accuracy:
            break
        x = y
   
    print('iterations: ', iterations)
def Method_simple_iterations(x, t):
    iterations = 0
    while True:
        iterations += 1
        f_x = f(x)
        y = x - t * (-f_x)
        print(y)
        if abs(y - x) < accuracy:
            break
        x = y
    print('iterations: ', iterations)

Method_simple_iterations(1, 0.3)

x_value = np.arange(0, 2.75, 0.25)
y_value = []
result = {}
for x in x_value:
    print (f'{x:.7f}  {f(x):.7f}')
    y_value.append(f(x))
    
fig, ax = plt.subplots()
ax.plot(x_value, y_value)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.grid(True)
plt.show()


        




