import numpy as np
import matplotlib.pyplot as plt

def U0x(x):
    return 1 - x


def schemeCross(x_limits, h, t_limits, little_tau):
    x_steps = int((x_limits[1] - x_limits[0]) / h) + 1
    t_steps = int((t_limits[1] - t_limits[0]) / little_tau) + 1
    
    U =np.zeros((t_steps, x_steps))
    lambda_ = little_tau**2 / h**2
    
    x = np.arange(x_limits[0], x_limits[1] + h, h)
    t = np.arange(t_limits[0], t_limits[1] + little_tau, little_tau)
    
    for j in range(t_steps):
        for i in range(x_steps-1):
           if j == 0:
               U[j, i] = U0x(x[i])
           elif j == 1:
               U[j, i] = U[0, i] + little_tau
           else:
               break;  
        U[j,0] = 1
    
    for j in range(1, t_steps - 1):
        for i in range(1, x_steps-1):
            U[j+1, i] = 2*(1-lambda_)*U[j,i] + lambda_*(U[j, i+1] + U[j, i-1]) - U[j-1, i]
            
    return  x, t, U

def schemeRotateH(x_limits, h, t_limits, little_tau):
    x_steps = int((x_limits[1] - x_limits[0]) / h) + 1
    t_steps = int((t_limits[1] - t_limits[0]) / little_tau) + 1
    
    U = np.zeros((t_steps, x_steps))
    lambda_ = little_tau**2 / (2 * h**2) 
    
    x = np.linspace(x_limits[0], x_limits[1], x_steps)
    t = np.linspace(t_limits[0], t_limits[1], t_steps)

    U[0, :] = U0x(x)  
    U[1, :] = U[0, :] + little_tau
    
    U[:, 0] = 1
    U[:, -1] = 0
    
    for j in range(1, t_steps - 1):
        S = np.zeros(x_steps)  
        T = np.zeros(x_steps)  
        S[0] = 0 
        T[0] = 1
        for i in range(1, x_steps - 1):
            denominator = 1 + 2*lambda_ - lambda_*S[i-1]
            S[i] = lambda_ / denominator
            T[i] = (lambda_ * T[i-1] - (1 + 2*lambda_) * U[j-1, i] + lambda_ * (U[j-1, i+1] + U[j-1, i-1]) + 2*U[j, i]) / denominator
         
        for i in range(x_steps - 2, 0, -1):
            U[j+1, i] = S[i] * U[j+1, i+1] + T[i]
    
    return x, t, U  
    

def schemeT(x_limits, h, t_limits, little_tau):
    
    x_steps = int(round((x_limits[1] - x_limits[0]) / h)) + 1
    t_steps = int(round((t_limits[1] - t_limits[0]) / little_tau)) + 1
  
    U = np.zeros((t_steps, x_steps))
    lambda_ = (little_tau**2) / (h**2)
    
    x = np.linspace(x_limits[0], x_limits[1], x_steps)
    t = np.linspace(t_limits[0], t_limits[1], t_steps)
     
    U[0, :] = U0x(x)  
    U[1, :] = U[0, :] + little_tau  
    
    U[:, -1] = 0         
    U[:, 0] = 1 
    
    for j in range(1, t_steps - 1):
        S = np.zeros(x_steps)
        T = np.zeros(x_steps)
        S[0] = 0 
        T[0] = 1
        
        for i in range(1, x_steps - 1):
            denominator = 1 + 2*lambda_ - lambda_*S[i-1]
            S[i] = lambda_ / denominator
            T[i] = (2*U[j, i] - U[j-1, i] + lambda_*T[i-1]) / denominator    
        U[j+1, -1] = 0   
        for i in range(x_steps - 2, 0, -1):
            U[j+1, i] = S[i] * U[j+1, i+1] + T[i]
        
    return x, t, U

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
t_limits = [0, 10]
little_tau = 0.01
h = 0.01


x1, t1, U1 = schemeCross(x_limits, h, t_limits, little_tau)
x2, t2, U2 = schemeRotateH(x_limits, h, t_limits, little_tau)
x3, t3, U3 = schemeT(x_limits, h, t_limits, little_tau)
drawGraph(x1, t1, U1, "Крест")
drawGraph(x2, t2, U2, "Перевернутый H")
drawGraph(x3, t3, U3, "T")