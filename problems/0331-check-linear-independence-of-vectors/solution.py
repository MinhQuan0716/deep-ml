import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    # Your code here
    tol = 1e-10 # Use as a check condition for Gaussian elimination
    if not vectors: return True
    if len(vectors) > len(vectors[0]): return False
    M = np.array(vectors, dtype = float,copy = True)
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

    return pivot_row == m