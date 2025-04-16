import numpy as np
import matplotlib.pyplot as plt

def U0x(x):
   return x + 2

def Ut0(t):
   return 2

def Ut1(t):
   return 3

def explicitScheme(x_limits, h, t_limits, tau, D):
   x_steps = int((x_limits[1] - x_limits[0]) / h) + 1
   t_steps = int((t_limits[1] - t_limits[0]) / tau) + 1
    
   U = np.zeros((t_steps, x_steps))
   lambda_value = tau * D / h**2
    
   x = np.linspace(x_limits[0], x_limits[1], x_steps)
   t = np.linspace(t_limits[0], t_limits[1], t_steps)
    
   U[0, :] = U0x(x)  
   U[:, 0] = Ut0(t)   
   U[:, -1] = Ut1(t)  
    
   for j in range(t_steps - 1):
      for i in range(1, x_steps - 1):
         U[j+1, i] = U[j, i] + lambda_value * (U[j, i+1] - 2*U[j, i] + U[j, i-1])
    
   return x, t, U, lambda_value

def implicitScheme(x_limits, h, t_limits, tau, D):
    x_steps = int((x_limits[1] - x_limits[0]) / h) + 1
    t_steps = int((t_limits[1] - t_limits[0]) / tau) + 1
    
    U = np.zeros((t_steps, x_steps))
    lambda_value = tau * D / h**2
    
    x = np.linspace(x_limits[0], x_limits[1], x_steps)
    t = np.linspace(t_limits[0], t_limits[1], t_steps)
    
    U[0, :] = U0x(x)
    U[:, 0] = Ut0(t)
    U[:, -1] = Ut1(t)
    
    for j in range(t_steps - 1):
         S = np.zeros(x_steps)
         T = np.zeros(x_steps)
         T[0] = Ut0(j)
         for i in range(1, x_steps - 1):
            denominator = 1 + lambda_value*2 - lambda_value*S[i-1]
            S[i] = lambda_value / denominator
            T[i] = (U[j, i] + lambda_value*T[i-1]) / denominator
    
         for i in range(x_steps-2, 0, -1):
            U[j+1, i] = S[i] * U[j+1, i+1] + T[i]
   
    return x, t, U
# функция отриосвки
def drawGraph(x, t, U, name):
   fig = plt.figure(figsize=(10,7))
   fig.canvas.manager.set_window_title(name)
   ax_3d = fig.add_subplot(projection='3d')
   x_gred, t_grid = np.meshgrid(x, t)
   ax_3d.plot_surface(x_gred, t_grid, U, cmap='plasma')
   ax_3d.set_xlabel('x')
   ax_3d.set_ylabel('t')
   ax_3d.set_zlabel('U')
   plt.show()
   
x_limits = [0, 1]
h = 0.05
t_limits = [0, 10]
little_tau = 0.00125
D = 1

x1, t1, U1, l1 = explicitScheme(x_limits, h, t_limits, little_tau, D)
x2, t2, U2 = implicitScheme(x_limits, h, t_limits, little_tau, D)
drawGraph(x1, t1, U1, 'Явная схема')
drawGraph(x2, t2, U2, 'Неявная схема')
print('lambda = ', l1)