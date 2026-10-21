import cmath 

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[complex|float]:
   
    val_trace = matrix[0][0] + matrix[1][1]
    det_val = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    
    b_coefficient = -val_trace
    
    eigenvalues = degree_2_polynomials(b_coefficient, det_val)
    return eigenvalues

def degree_2_polynomials(b: float, c: float) -> list[complex|float]:
    delta = (b**2) - (4*c)
    

    first = (-b + cmath.sqrt(delta)) / 2
    second = (-b - cmath.sqrt(delta)) / 2
    
    
    result = []
    for root in (first, second):
        if root.imag == 0:
            result.append(root.real)
        else:
            result.append(root)
            
    return result
