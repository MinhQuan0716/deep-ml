def cofactor_expansion(m:list[list[float]]) -> float:
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    total = 0.0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in m[1:]]
        sign = (-1) ** j
        total += sign * cofactor_expansion(minor) * m[0][j]
    return total
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    # Your code here
    det_val = cofactor_expansion(matrix)
    trace = 0.0 
    n = len(matrix)
    for i in range (n):
        trace += matrix[i][i]

    return (det_val,trace)
    pass