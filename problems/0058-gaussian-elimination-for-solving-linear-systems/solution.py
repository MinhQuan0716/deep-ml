import numpy as np
def partial_pivot(M:np.ndarray,n):
      for i in range(n):
        pivot_row = i +  int(np.argmax(np.abs(M[i:,i])))
        if pivot_row != i:
            M[[pivot_row,i]] = M[[i,pivot_row]]
        for j in range(i + 1, n):
            factor = M[j][i] / M[i][i]
            M[j] -= factor*M[i]
def back_subtitue(M:np.ndarray,n) -> list:
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_val = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - sum_val) / M[i][i]
    return x
    
def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :return: Solution vector x
    """
    n = len(A[0])
    M = np.column_stack((A, b)).astype(float)
    partial_pivot(M,n)
    x = back_subtitue(M,n)
    return x
