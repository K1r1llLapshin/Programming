import numpy as np

def f(x, y):
    return (y**2)*np.cos(1+x)

def MaxDiff(last_res,new_res):
    max_diff = 0
    for last in last_res:
        for i in range(len(new_res)):
            if last[0] == new_res[i][0] and abs(last[1] - new_res[i][1]) > max_diff:
                max_diff = abs(last[1] - new_res[i][1])
                break
    return max_diff

def Euler(points, h):
    return points[0] + h*points[2]

def Runge_Kutta(points, h):
    k1 = h*f(points[0], points[1])
    k2 = h*f(points[0] + h/2, points[1] + k1/2)
    k3 = h*f(points[0] + h/2, points[1] + k2/2)
    k4 = h*f(points[0] + h, points[1] + k3)
    delta_g = (k1 + 2*k2 + 2*k3 + k4) / 6
    return points[2] + delta_g

def Adams3(starting_condition, count_point, interval, epsilon, last_res):
    h = (interval[1] - interval[0]) / count_point
    x = np.arange(interval[0], interval[1]+h, h)
    g = [starting_condition[2]]
    y = [(x[0], starting_condition[1])]
    
    for i in range(0, 2):
        y.append((x[i+1], Euler([x[i], y[i][1], g[i]], h)))
        g.append(Runge_Kutta([x[i], y[i][1], g[i]], h))
        
    for i in range(2, len(x)-1):
        y.append((x[i+1], y[i][1] + h*(23*g[i] - 16*g[i-1] + 5*g[i-2])/12))
        g.append(g[i] + h*(23*f(x[i], y[i][1]) - 16*f(x[i-1], y[i-1][1]) + 5*f(x[i-2], y[i-2][1]))/12)
    
    max_diff = MaxDiff(last_res, y)
    if max_diff < epsilon and max_diff != 0:
        return last_res, y, count_point 
    else:
        return Adams3(starting_condition, count_point*2, interval, epsilon, y)
    

def Adams4(starting_condition, count_point, interval, epsilon, last_res):
    h = (interval[1] - interval[0]) / count_point
    x = np.arange(interval[0], interval[1]+h, h)
    g = [starting_condition[2]]
    y = [(x[0], starting_condition[1])]
    
    for i in range(0, 3):
        y.append((x[i+1], Euler([x[i], y[i][1], g[i]], h)))
        g.append(Runge_Kutta([x[i], y[i][1], g[i]], h))
        
    for i in range(3, len(x)-1):
        y.append((x[i+1], y[i][1] + h*(55*g[i] - 59*g[i-1] + 37*g[i-2] - 9*g[i-3])/24))
        g.append(g[i] + h*(55*f(x[i], y[i][1]) - 59*f(x[i-1], y[i-1][1]) + 37*f(x[i-2], y[i-2][1])- 9*f(x[i-3], y[i-3][1]))/24)
    
    max_diff = MaxDiff(last_res, y)
    if max_diff < epsilon and max_diff != 0:
        return last_res, y, count_point 
    else:
        return Adams4(starting_condition, count_point*2, interval, epsilon, y)
    
starting_condition = [0, 0, 1]
count_point = 4
interval = [0, 0.5]
epsilon = 0.001
last_res= []

last, y, c = Adams4(starting_condition, count_point, interval, epsilon, last_res)
print(c)

print(f'{'x_i':<10}{'y_i last':<20}{'y_i now':<20}{"рызница":<20}')


for i in range(len(y)):
    found = False
    for j in range(len(last)):
        if last[j][0] == y[i][0]:  
            diff = abs(y[i][1] - last[j][1])
            print(f'{y[i][0]:<10.4f} {last[j][1]:<20.4f} {y[i][1]:<20.4f} {diff:<20.4f}')
            found = True
            break 
    if not found: 
        print(f'{y[i][0]:<10.4f} {"---":<20} {y[i][1]:<20.4f} {"---":<20}')