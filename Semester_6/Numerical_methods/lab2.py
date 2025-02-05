import numpy as np

def Gauss_method(A, b, x_real):
    n = b.size
    x = np.zeros(n)
    
    for i in range(n):
        i_new = np.argmax(abs(A[i:, i])) + i
        A[[i, i_new]] = A[[i_new, i]]
        b[[i, i_new]] = b[[i_new, i]]
               
        for j in range(i + 1, n):
            k =  A[i, i]/ A[j, i]   
            A[j, :] = A[i, :] - k * A[j, :]  
            b[j] = b[i] - k * b[j] 

    for i in range(n - 1, -1, -1):  
        b[i] -= np.dot(A[i, i + 1:], x[i + 1:])  
        x[i] = b[i] / A[i, i]  

    print(f'Матрица:\n"{A}\n\nОтвет:{x}\n')
    print("Погрешность: ", "{:e}".format(np.linalg.norm(x_real - x)),'\n')
    
def Seidel_method(A, b, epsilon=1e-10):
    n = len(A)
    x = np.zeros(n)  
    converge = False
    it = 0
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            it += 1
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = np.linalg.norm(x_new - x) <= epsilon
        error = np.linalg.norm(x_new - x)
        x = x_new
    print(f'Итераций: {it}\nОтвет: {x}')
    return error

A = np.array([[2.12, 0.42, 1.34, 0.88],
             [0.42, 3.95, 1.87, 0.43],
             [1.34, 1.87, 2.98, 0.46],
             [0.88, 0.43, 0.46, 4.44]])

b = np.array([5.56, 2.55, 0.64, 15.03])
x_real = np.array([2.5, 1, -2, 3])




