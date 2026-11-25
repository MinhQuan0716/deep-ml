def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    det_val = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    if det_val == 0:
        return None
    else:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        result[0][0] = d*(1/det_val)
        result[0][1] = -b*(1/det_val)
        result[1][0] = -c*(1/det_val)
        result[1][1] = a*(1/det_val)
    return result
    pass