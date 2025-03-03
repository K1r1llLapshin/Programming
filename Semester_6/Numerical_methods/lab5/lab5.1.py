import numpy as np

def f(x, y):
    return (1 - y**2) * np.cos(x) + 0.6 * y


def MaxDiff(last_res,new_res):
    max_diff = 0
    for last in last_res:
        for i in range(len(new_res)):
            if last[0] == new_res[i][0] and abs(last[1] - new_res[i][1]) > max_diff:
                max_diff = abs(last[1] - new_res[i][1])
                break
    return max_diff

def Euler_Cauchy(starting_condition, count_point, interval, epsilon, last_res):
    h = (interval[1] - interval[0]) / count_point
    x = np.arange(interval[0], interval[1], h)
    y_n = starting_condition[1]
    y = [(starting_condition[0], starting_condition[1])]
    for x_n in x:
        dy = f(x_n, y_n)
        tilda_y = y_n + h*dy
        tilda_dy = f(x_n+h, tilda_y)
        y_n = y_n + h * (dy + tilda_dy) / 2
        y.append((x_n + h, y_n))
        
    max_diff = MaxDiff(last_res, y)
    if max_diff < epsilon and max_diff != 0:
        return last_res, y, count_point 
    else:
        return Euler_Cauchy(starting_condition, count_point*2, interval, epsilon, y)

def Runge_Kutta(starting_condition, count_point, interval, epsilon, last_res):
    h = (interval[1] - interval[0]) / count_point
    x = np.arange(interval[0], interval[1], h)
    y_n = starting_condition[1]
    y = [(starting_condition[0], starting_condition[1])]
    
    for x_n in x:
        k1 = h*f(x_n, y_n)
        k2 = h*f(x_n + h/2, y_n + k1/2)
        k3 = h*f(x_n + h/2, y_n + k2/2)
        k4 = h*f(x_n + h, y_n + k3)
        delta_y = (k1 + 2*k2 + 2*k3 + k4) / 6
        y_n = y_n + delta_y
        y.append((x_n + h, y_n))
        
        
    max_diff = MaxDiff(last_res, y)
    if max_diff < epsilon and max_diff != 0:
        return last_res, y, count_point 
    else:
        return Runge_Kutta(starting_condition, count_point*2, interval, epsilon, y)     

        
starting_condition = [0, 0]
count_point = 4
interval = [0, 0.5]
epsilon = 0.001
last_res= []

last, y, c = Runge_Kutta(starting_condition, count_point, interval, epsilon, last_res)
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