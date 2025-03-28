import numpy as np
import matplotlib.pyplot as plt 

def Ux0(x):
    return 0 if x >= 0.5 else 4

def ArtificialViscosity(x_limits, h, t_limits, little_tau, epsilon):
    x_steps = int((x_limits[1] - x_limits[0]) / h) + 1
    t_steps = int((t_limits[1] - t_limits[0]) / little_tau) + 1
    
    U = np.zeros((t_steps, x_steps))
    
    x = np.arange(x_limits[0], x_limits[1] + h, h) 
    t = np.arange(t_limits[0], t_limits[1] + little_tau, little_tau)
    
    for i in range(x_steps):
        U[0][i] = Ux0(x[i])
        
    for j in range(t_steps-1):
        for i in range (1, x_steps - 1):
            U[j+1][i] = U[j][i] - little_tau / h * U[j][i] * (U[j][i] - U[j][i-1]) 
            - epsilon ** 2 * little_tau / (2 * h ** 3) * (U[j][i+1] - U[j][i-1]) * (U[j][i+1] - U[j][i] + U[j][i-1])
    
    return U, x, t 
    
def ConservativeScheme(x_limits, h, t_limits, little_tau, epsilon):
    x_steps = int((x_limits[1] - x_limits[0]) / h) + 1
    t_steps = int((t_limits[1] - t_limits[0]) / little_tau) + 1
    
    U = np.zeros((t_steps, x_steps))
    
    x = np.arange(x_limits[0], x_limits[1] + h, h) 
    t = np.arange(t_limits[0], t_limits[1] + little_tau, little_tau)
    
    for i in range(x_steps):
        U[0][i] = Ux0(x[i])
        
    for j in range(t_steps-1):
        for i in range (1, x_steps):
            U[j+1][i] = U[j][i] - little_tau / (2*h) * (U[j][i]**2 - U[j][i-1]**2) 
    
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
    

x_limits = [0, 1]
t_limits = [0, 1]
h = 0.05
little_tau = 0.001
epsilon = 0.01


U1, x1, t1 = ArtificialViscosity(x_limits, h, t_limits, little_tau, epsilon)
U2, x2, t2 = ConservativeScheme(x_limits, h, t_limits, little_tau, epsilon)
g = h / U1.max()

if little_tau <= g:
    print ('Устойчивость выполняется')
else:
    print ('Устойчивость не выполняется')

drawGraph(x1, t1, U1, "Искустенная вязкость")
drawGraph(x2, t2, U2, "Консервативная схема")