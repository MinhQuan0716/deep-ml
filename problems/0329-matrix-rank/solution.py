import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Your code here
    M = np.array(A, dtype=float, copy=True)
    if M.size == 0: return 0
    m, n = M.shape
    pivot_row = 0
    for col in range(n):
        if pivot_row == m:
            break
        col_splice= M[pivot_row:,col]
        max_row = pivot_row + int(np.argmax(np.abs(col_splice)))
        if np.abs(M[max_row,col])<=tol:
            continue
        M[[pivot_row, max_row]] = M[[max_row, pivot_row]]
        for r in range(pivot_row + 1,m):
           factor = M[r,col]/M[pivot_row,col]
           M[r]  = M[r] - (factor * M[pivot_row])
        pivot_row += 1

    return pivot_row