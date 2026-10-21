def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []
        
    rows = len(matrix)
    cols = len(matrix[0])
    means = []
    
    if mode == "row":
        for r in range(rows):
            sumRow = 0                
            for c in range(cols):    
                sumRow += matrix[r][c]
            
            row_mean = sumRow / cols  
            means.append(row_mean)
            
    elif mode == "column":
        for c in range(cols):
            sumCol = 0                
            for r in range(rows):     
                sumCol += matrix[r][c]
                
            col_mean = sumCol / rows  
            means.append(col_mean)
            
    return means