import numpy as np
import matplotlib.pyplot as plt 

# функции
def Ux0(x):
    return 2*(x**2) + 2*x

def U0t(t):
    return t**2 + 2*t

def U1t(t):
    return t**2 + 2*t + 4

def f(x):
    return 2*x

# Для полуплоскости 
def scheme1_HalfPlane(x_start, x_end, h, t, small_tau, a):
    x_steps = int((x_end - x_start) / h) + 1
    t_steps = int(t / small_tau) + 1
    
    U = np.zeros((t_steps, x_steps + t_steps))
    f_arr = np.zeros(x_steps + t_steps)
    
    my_lambda = a * small_tau / h

    x = np.arange(x_start - t_steps * h, x_end + h, h)
    t = np.arange(0, t + small_tau, small_tau)
    
    for i in range(x_steps + t_steps):
        f_arr[i] = f(x[i])  
        U[0][i] = Ux0(x[i]) 
        
    for i in range(t_steps - 1): 
        for j in range(1, x_steps + t_steps):
            U[i+1][j] = my_lambda * U[i][j-1] + (1 - my_lambda) * U[i][j] + small_tau * f_arr[j]
    
    nU = U[:, t_steps:t_steps + x_steps]
    
    return nU, x[t_steps:t_steps + x_steps], t

def scheme2_HalfPlane(x_start, x_end, h, t, small_tau, a):
    x_steps = int((x_end - x_start) / h) + 1
    t_steps = int(t / small_tau) + 1
    
    U = np.zeros((t_steps, x_steps + t_steps))
    f_arr = np.zeros(x_steps + t_steps)
    
    my_lambda = a * small_tau / h

    x = np.arange(x_start, x_end + t_steps * h + h, h)
    t = np.arange(0, t + small_tau, small_tau)
    
    for i in range(x_steps + t_steps):
        f_arr[i] = f(x[i])  
        U[0][i] = Ux0(x[i]) 
        
    for i in range(t_steps - 1): 
        for j in range(x_steps + t_steps - 2, -1, -1):
            U[i+1][j] = U[i][j] * (1 + my_lambda) - my_lambda * U[i][j+1] + small_tau * f_arr[j]
    
    nU = U[:, :x_steps + 1]
    
    return nU, x[:x_steps + 1], t

# Для прямоугольной области 
def scheme1_Rectangle(x_start, x_end, h, t_start, t_end, small_tau, a):
    x_steps = int((x_end - x_start) / h) + 1
    t_steps = int((t_end - t_start) / small_tau) +1
    
    U = np.zeros((t_steps, x_steps))
    f_arr = np.zeros(x_steps)
    
    my_lambda = a * small_tau / h

    x = np.arange(x_start, x_end + h, h)
    t = np.arange(t_start, t_end + small_tau, small_tau)
    
    for i in range(x_steps):
        f_arr[i] = f(x[i])
        U[0][i] = Ux0(x[i]) 
    
    for i in range(t_steps):
        U[i][0] = U0t(t[i])   
    
    for i in range(t_steps - 1):
        for j in range(1, x_steps):
            U[i+1][j] = my_lambda * U[i][j-1] + (1 - my_lambda) * U[i][j] + small_tau * f_arr[j]
    
    return U, x, t

def scheme2_Rectangle(x_start, x_end, h, t_start, t_end, small_tau, a):
    x_steps = int((x_end - x_start) / h) + 1
    t_steps = int((t_end - t_start) / small_tau) + 1
    
    U = np.zeros((t_steps, x_steps))
    f_arr = np.zeros(x_steps)
    
    my_lambda = a * small_tau / h

    x = np.arange(x_start, x_end + h, h)
    t = np.arange(t_start, t_end + small_tau, small_tau)
    
    for i in range(x_steps):
        f_arr[i] = f(x[i])
        U[0][i] = Ux0(x[i]) 
    
    for i in range(t_steps):
        U[i][x_steps - 1] = U1t(t[i])   
    
    for i in range(t_steps - 1):
        for j in range(x_steps - 2, -1, -1):
            U[i+1][j] = U[i][j] * (1 + my_lambda) - my_lambda * U[i][j+1] + small_tau * f_arr[j]
    
    return U, x, t

def scheme3_Rectangle(x_start, x_end, h, t_start, t_end, small_tau, a):
    x_steps = int((x_end - x_start) / h) + 1
    t_steps = int((t_end - t_start) / small_tau) + 1
    
    U = np.zeros((t_steps, x_steps))
    f_arr = np.zeros(x_steps)
    
    my_lambda = a * small_tau / h

    x = np.arange(x_start, x_end + h, h)
    t = np.arange(t_start, t_end + small_tau, small_tau)
    
    for i in range(x_steps):
        f_arr[i] = f(x[i])
        U[0][i] = Ux0(x[i]) 
    
    for i in range(t_steps):
        U[i][0] = U0t(t[i])   
    
    for i in range(t_steps - 1):
        for j in range(1, x_steps):
            U[i+1][j] =(U[i][j] + my_lambda * U[i+1][j-1] + small_tau * f_arr[j]) / (1 + my_lambda)
    
    return U, x, t

def scheme4_Rectangle(x_start, x_end, h, t_start, t_end, small_tau, a):
    x_steps = int((x_end - x_start) / h) + 1
    t_steps = int((t_end - t_start) / small_tau) + 1
    
    U = np.zeros((t_steps, x_steps))
    f_arr = np.zeros(x_steps)
    
    my_lambda = a * small_tau / h
    
    x = np.arange(x_start, x_end + h, h) 
    t = np.arange(t_start, t_end + small_tau, small_tau)  
    
    for i in range(x_steps):
        f_arr[i] = f(x[i])
        U[0][i] = Ux0(x[i])  
    
    for i in range(t_steps):
        U[i][x_steps - 1] = U1t(t[i])
    
    for i in range(t_steps - 1):  
        for j in range(x_steps - 2, -1, -1):  
            U[i+1][j] = (U[i][j] - my_lambda * U[i+1][j+1] + small_tau * f_arr[j]) / (1 - my_lambda)
    
    return U, x, t

###def scheme_Rectangle(x_start, x_end, h, t_start, t_end, small_tau, a):
    x_steps = int((x_end - x_start) / h) + 1
    t_steps = int((t_end - t_start) / small_tau) + 1
    
    U = np.zeros((t_steps, x_steps))
    f_arr = np.zeros(x_steps)
    
    my_lambda = a * small_tau / h
    
    x = np.arange(x_start, x_end + h, h) 
    t = np.arange(t_start, t_end + small_tau, small_tau)  
    
    for i in range(x_steps):
            f_arr[i] = f(x[i] + h/2)
            U[0][i] = Ux0(x[i])  
            
    if a < 0:  
        for i in range(t_steps):
            U[i][x_steps - 1] = U1t(t[i])
        
        for i in range(t_steps - 1):  
            for j in range(x_steps - 1, -1, -1):  
                U[i+1][j-1] = ((1 + my_lambda) * (U[i+1][j] - U[i][j-1]) - (1 - my_lambda) * U[i][j] - 2 * small_tau * f_arr[j]) / (my_lambda - 1)
    else:
        for i in range(t_steps):
            U[i][0] = U0t(t[i])
        
        for i in range(t_steps - 1):  
            for j in range(1, x_steps):  
                U[i+1][j] = ((1 - my_lambda) * (U[i][j] - U[i+1][j-1]) + (1 + my_lambda) * U[i][j-1] + 2 * small_tau * f_arr[j]) / (1 + my_lambda)
    
    return U, x, t 


# функция отриосвки
def drawGraph(x, t, U, name):
    fig = plt.figure(figsize=(8,6))
    fig.canvas.manager.set_window_title(name)
    ax_3d = fig.add_subplot(projection='3d')
    x_gred, t_grid = np.meshgrid(x, t)
    ax_3d.plot_surface(x_gred, t_grid, U, cmap='plasma')
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('t')
    ax_3d.set_zlabel('U')
    plt.show()
    
# Данные и результат
x_start = 0
x_end = 1
t_start = 0
t_end = 10
h = 0.1
small_tau = 0.05
a1 = 2
a2 = -2
U1, x1, t1 = scheme1_Rectangle(x_start, x_end, h, t_start, t_end, small_tau, a1)
U2, x2, t2 = scheme2_Rectangle(x_start, x_end, h, t_start, t_end, small_tau, a2)
U3, x3, t3 = scheme3_Rectangle(x_start, x_end, h, t_start, t_end, small_tau, a1)
U4, x4, t4 = scheme4_Rectangle(x_start, x_end, h, t_start, t_end, small_tau, a2)
U5, x5, t5 = scheme1_HalfPlane(x_start, x_end, h, t_end, small_tau, a1)
U6, x6, t6 = scheme2_HalfPlane(x_start, x_end, h, t_end, small_tau, a2)

drawGraph(x1, t1, U1, "правый нижний угол")
drawGraph(x2, t2, U2, "левый нижний угол")
drawGraph(x3, t3, U3, "правый верхний угол")
drawGraph(x4, t4, U4, "левый верхний угол")
drawGraph(x5, t5, U5,"правый нижний угол полуплоскость")
drawGraph(x6, t6, U6,"левый нижний угол полуплоскость")
