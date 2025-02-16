import numpy as np

def f(x):
    return np.cos(x)**2

def df(x):
    return -2*np.cos(x)*np.sin(x)

def ddf(x):
    return 2*np.sin(x)**2-2*np.cos(x)**2

def corD(a, b, count_point):
    print("точная производная")
    h = (b-a)/(count_point-1)
    x_point = np.arange(a, b+h, h)
    for x in x_point:
        print(f'{x:<10} {df(x):.4f}') 

def corDD(a, b, count_point):
    print("точная вторая производная")
    h = (b-a)/(count_point-1)
    x_point = np.arange(a, b+h, h)
    for x in x_point:
        print(f'{x:<10} {ddf(x):.4f}') 
                
def Derived(a, b, count_point):
    print("левая производная")
    h = (b-a)/(count_point-1)
    x_point = np.arange(a, b+h, h)
    
    correctD = []
    correctDD = []
    leftD = []
    rightD = [] 
    midD = []
    secD = []
    for i in range(x_point.size):
        correctD.append(round(df(x_point[i]), 4))
        correctDD.append(round(ddf(x_point[i]), 4))
        leftD.append('None' if i == 0 else round((f(x_point[i]) - f(x_point[i - 1])) / h, 4))
        rightD.append('None' if i == x_point.size - 1 else round((f(x_point[i + 1]) - f(x_point[i])) / h, 4))
        midD.append('None' if i == 0 or i == x_point.size - 1 else round((f(x_point[i + 1]) - f(x_point[i - 1])) / (2 * h), 4))
        secD.append('None' if i == 0 or i == x_point.size - 1 else round((f(x_point[i - 1]) - 2 * f(x_point[i]) + f(x_point[i + 1])) / h**2, 4))
    return  correctD, correctDD, leftD, rightD, midD, secD, x_point
     
correctD, correctDD, leftD, rightD, midD, secD, x_point = Derived(0, 1, 5)
error_l, error_r, error_m, error_sec = [], [], [], [] 
print(f"{'x_k':<10}{'производная слева':<25}{'производная справа':<25}{'производная центр':<25}{'вторая производная':<25}{'точная производная':<25} {'вторая точная производная'}")
for i in range(5):
    print(f"{x_point[i]:<10}{leftD[i]:<25}{rightD[i]:<25}{midD[i]:<25}{secD[i]:<25}{correctD[i]:<25} {correctDD[i]}")
    error_l.append(round(abs(correctD[i] - leftD[i]),4) if leftD[i] != "None" else 'None')
    error_r.append(round(abs(correctD[i] - rightD[i]),4) if rightD[i] != "None" else 'None')
    error_m.append(round(abs(correctD[i] - midD[i]),4) if midD[i] != "None" else 'None')
    error_sec.append(round(abs(correctDD[i] - secD[i]),4) if secD[i] != "None" else 'None') 

print("\nПогрешность")
print(f"{'x_k':<10}{'производная слева':<25}{'производная справа':<25}{'производная центр':<25}{'вторая производная':<25}")
for i in range(5):
    print(f"{x_point[i]:<10}{error_l[i]:<25}{error_r[i]:<25}{error_m[i]:<25}{error_sec[i]:<25}")
      
      
      
      