def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    row = len(matrix)
    col = len(matrix[0])
    
    for r in range(row):          # Added range()
        for c in range(col):      # Added range() and fixed typo (col instead of cols)
            matrix[r][c] = scalar * matrix[r][c]

    return matrix                 # Aligned properly