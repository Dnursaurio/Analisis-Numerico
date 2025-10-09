import numpy as np

def lu_basico(A):
    """
    Descomposición LU básica
    """
    n = A.shape[0]
    L = np.identity(n)
    U = A.copy().astype(float)
    
    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]
    
    return L, U

A = np.array([[1,4,3,5],[6,1,3,7],[2,5,4,1],[3,5,6,1]])

L, U = lu_basico(A)

print("A =\n", A)
print("L =\n", L)
print("U =\n", U)