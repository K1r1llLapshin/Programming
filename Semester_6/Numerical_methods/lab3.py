from numpy import log
epsilon = 10**-5

def f(x):
    return 3**(2*x)

def F(x):
    return f(x) / (2 * log(3))

def RelativeError(I, I_h):
    return abs((I - I_h) / I) * 100

def LeftRectangle(a, b, n, I_old):
    h = (b - a)/ n
    I_now = 0
    for i in range(n):
         I_now += h * f(a + i * h)
    
    if abs(I_now - I_old) < epsilon:
        return I_now, h, n
    else:
        return LeftRectangle(a, b, 2*n, I_now)
    

def RightRectangle(a, b, n, I_old):
    h = (b - a)/ n
    I_now = 0
    for i in range(1, n+1):
         I_now += h * f(a + i * h)
    
    if abs(I_now - I_old) < epsilon:
        return I_now, h, n
    else:
        return RightRectangle(a, b, 2*n, I_now)
              
def MidRectangle(a, b, n, I_old):
    h = (b - a)/ n
    I_now = 0
    for i in range(n):
         I_now += h * f(a + i * h + h/2)
    
    if abs(I_now - I_old) < epsilon:
        return I_now, h, n
    else:
        return MidRectangle(a, b, 2*n, I_now)
    
def Trapezoids(a, b, n, I_old):
    h = (b - a)/ n
    I_now = h * (f(a) + f(b)) / 2
    for i in range(1, n):
         I_now += h * f(a + i * h)
    
    if abs(I_now - I_old) < epsilon:
        return I_now, h, n
    else:
        return Trapezoids(a, b, 2*n, I_now)

def Simpson(a, b, n, I_old):
    h = (b - a)/ n
    I_now = (f(a)+f(b))*h/3
    
    for i in range(1, n):
        I_now += 4 * f(a + i * h) * h / 3 if i % 2 != 0 else 2 * f(a + i * h) * h / 3
     
    if abs(I_now - I_old) < epsilon:
        return I_now, h, n
    else:
        return Simpson(a, b, 2*n, I_now)


metods = [LeftRectangle, RightRectangle, MidRectangle, Trapezoids, Simpson]
a = 0
b = 1
n_n = 2
I = F(b) - F(a)
for metod in metods:
    n = n_n
    I_n, h, n = metod(a, b, n, 0)
    delta = RelativeError(I, I_n)
    print(f"\t\tМетод {metod.__name__}\nПрибличенное решение: {I_n:.5f}\nВеличина последнего шага: {h:.10f}\nКол-во точек разбиения: {n}\nОтносительная погрешность: {delta:.6f} %\n\n")

