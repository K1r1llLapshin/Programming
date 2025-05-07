import numpy as np
import matplotlib.pyplot as plt

def Ux(x, t):
    return x + t

def Uy(y, t):
    return t + y

def f(x, y):
    return 2*x-y

def simpleIterationMethod(x_limit, y_limit, sgrid_size, epsilon):
    h =  (x_limit[1] - x_limit[0]) / sgrid_size[0]
    tau = (y_limit[1] - y_limit[0]) / sgrid_size[1]
    x = np.arange(x_limit[0], x_limit[1]+h, h)
    y = np.arange(y_limit[0], y_limit[1]+h, tau)
    U_old = np.zeros((sgrid_size[1]+1, sgrid_size[0]+1))
    
    U_old[0, :] = Ux(x, y_limit[0])
    U_old[-1, :] = Ux(x, y_limit[1])
    U_old[:, 0] = Uy(y, x_limit[0])
    U_old[:, -1] = Uy(y, x_limit[1])
    
    while True:
        U_new = U_old.copy()
        for j in range(1, sgrid_size[1]):
            for i in range(1, sgrid_size[0]):
                U_new[j, i] = (U_old[j-1, i] + U_old[j+1, i] + U_old[j, i-1] + U_old[j, i+1] - h*tau*f(x[i], y[j]))/4
        
        diff = np.linalg.norm(U_new - U_old)
        if diff < epsilon:
            break
        else:
            U_old = U_new
            
    return x, y, U_new


def SeidelMethod(x_limit, y_limit, sgrid_size, epsilon):
    h =  (x_limit[1] - x_limit[0]) / sgrid_size[0]
    tau = (y_limit[1] - y_limit[0]) / sgrid_size[1]
    x = np.arange(x_limit[0], x_limit[1]+h, h)
    y = np.arange(y_limit[0], y_limit[1]+h, tau)
    U_old = np.zeros((sgrid_size[1]+1, sgrid_size[0]+1))
    
    U_old[0, :] = Ux(x, y_limit[0])
    U_old[-1, :] = Ux(x, y_limit[1])
    U_old[:, 0] = Uy(y, x_limit[0])
    U_old[:, -1] = Uy(y, x_limit[1])
    
    while True:
        U_new = U_old.copy()
        for j in range(1, sgrid_size[1]):
            for i in range(1, sgrid_size[0]):
                U_new[j, i] = (U_new[j-1, i] + U_new[j+1, i] + U_new[j, i-1] + U_new[j, i+1] - h*tau*f(x[i], y[j]))/4
        
        diff = np.linalg.norm(U_new - U_old)
        if diff < epsilon:
            break
        else:
            U_old = U_new
            
    return x, y, U_new    

def drawGraph(x, t, U, name1, name2):
   fig = plt.figure(figsize=(10,7))
   fig.canvas.manager.set_window_title(name1)
   ax_3d = fig.add_subplot(projection='3d')
   x_gred, t_grid = np.meshgrid(x, t)
   ax_3d.plot_surface(x_gred, t_grid, U, cmap='plasma')
   ax_3d.set_title(name2)
   ax_3d.set_xlabel('x')
   ax_3d.set_ylabel('y')
   ax_3d.set_zlabel('U')
   plt.show()
   
#-----------------------------------------------------------

x_limit = [0, 10]
y_limit = [0, 10]
sgrid_size_little = [5, 5]
sgrid_size_big = [10, 10]
epsilon= 0.01

x1, y1, U1 = simpleIterationMethod(x_limit, y_limit, sgrid_size_little, epsilon)
drawGraph(x1, y1, U1, "Результат с маленьким шагом", "сетка 5*5")

x2, y2, U2 = simpleIterationMethod(x_limit, y_limit, sgrid_size_big, epsilon)
drawGraph(x2, y2, U2, "Результат с большим шагом", "сетка 10*10")

x3, y3, U3 = SeidelMethod(y_limit, x_limit, sgrid_size_little, epsilon)
drawGraph(x3, y3, U3, "Результат методом Зейделя с маленьким шагом", "сетка 5*5")

x4, y4, U4 = SeidelMethod(y_limit, x_limit, sgrid_size_big, epsilon)
drawGraph(x4, y4, U4, "Результат методом Зейделя с большим шагом", "сетка 10*10")

