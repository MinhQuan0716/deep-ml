import numpy as np

def calculate_coff(coeffs: list, x: float) -> tuple[float,float]:
    val_result = 0
    derivative_result = 0
    for i in range(len(coeffs)):
        n = len(coeffs) - 1 - i 
        val_result += x**n*coeffs[i] 
        if(n == 0):
            continue
        derivative_result += x**(n-1)*n*coeffs[i]
    return (val_result,derivative_result)
def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    (coff_h,derivative_coff_h) = calculate_coff(h_coeffs,x)
    (coff_g,derivative_coff_g) = calculate_coff(g_coeffs,x)
    result = float((coff_h * derivative_coff_g - coff_g * derivative_coff_h)/(coff_h**2))
    return result