import numpy as np
from numpy import linalg as LA

def is_pos_def(x):
    return np.all(np.linalg.eigvals(x)>0)

def conjugate_gradient(A, b):
    if (is_pos_def(A) == False) | (A != A.T).any():
        raise ValueError('Matriks A harus simetris definit positif (eigenvalue bernilai positif)')
    r = b 
    k = 0
    x = np.zeros(A.shape[-1])
    while LA.norm(r) > 0.1 :
        if k == 0:
            p = r
        else: 
            gamma = - (p @ A @ r)/(p @ A @ p)
            p = r + gamma * p
        alpha = (p @ r) / (p @ A @ p)
        x = x + alpha * p
        r = r - alpha * (A @ p)
        k =+ 1
    return x

A = np.array([[3, -1, 1], [-1, 6, 2], [1, 2, 7]])
b = np.array([1, 0, 4])
x0 = np.array([0, 0, 0])


print(conjugate_gradient(A, b))