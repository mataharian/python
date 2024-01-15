import numpy as np

A = [[3, -1, 1],
     [-1, 6, 2],
     [1, 2, 7]]
b = [1, 0, 4]


def conjugate_gradient(A, b, x = np.array([0] * len(b)), tol = 1e-3):
    C = np.identity(len(x))
    r = b - (A @ x)
    w = np.linalg.inv(C) @ r
    v = np.linalg.inv(C) @ w
    alpha = np.dot(w, w)
    it = 0
    print(f"Iterasi {it}: {x}")
    while np.linalg.norm(v, np.inf) > tol:
        u = A @ v
        t = alpha / np.dot(u, v)
        x = x + t * v
        r = r - t * u
        w = np.linalg.inv(C) @ r
        beta = np.dot(w, w)
        it += 1
        print(f"Iterasi {it}: {x}")
        if abs(beta) < tol and np.linalg.norm(r, np.inf) < tol:
          break
        s = beta / alpha
        v = np.linalg.inv(C.transpose()) @ w + s * v
        alpha = beta
    return x

print(conjugate_gradient(A, b))