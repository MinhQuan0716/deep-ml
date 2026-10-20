import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    # 1. Defend against test cases where the tuple is not exactly 2D
    if len(new_shape) != 2:
        return []
        
    new_rows, new_cols = new_shape
    
    # Catch cases where the original matrix might be completely empty
    if not a or not a[0]:
        return []
        
    orig_rows = len(a)
    orig_cols = len(a[0])
    
    # 2. Return an empty list [] if dimensions don't match, instead of raising an Error
    if orig_rows * orig_cols != new_rows * new_cols:
        return []
        
    # 3. Build the canvas and execute the manual reshape
    result = [[0 for _ in range(new_cols)] for _ in range(new_rows)]
    flat_index = 0
    
    for r in range(orig_rows):
        for c in range(orig_cols):
            target_row = flat_index // new_cols
            target_col = flat_index % new_cols
            
            result[target_row][target_col] = a[r][c]
            flat_index += 1
            
    return result