def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    row = len(a)
    col = len(a[0])
    result = [[0 for _ in range(row)]  for _ in range(col)]
    for r  in range(row):
        for c in range(col):
            result[c][r] = a[r][c]
    return  result
    pass