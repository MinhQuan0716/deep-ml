import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Compute derivative of composite functions using chain rule.
    
    Args:
        functions: List of function names (applied right to left)
                  Available: 'square', 'sin', 'exp', 'log'
        x: Point at which to evaluate derivative
    
    Returns:
        Derivative value at x
    
    Example:
        ['sin', 'square'] represents sin(x²)
        ['exp', 'sin', 'square'] represents exp(sin(x²))
    """
    # Your code here
    ops = {
        'sin': (lambda u: np.sin(u), lambda u: np.cos(u)),
        'square': (lambda u: u**2, lambda u: 2*u),
        'exp': (lambda u: np.e**u, lambda u: np.e**u),
        'log': (lambda u: np.log(u), lambda u: 1/u)
    }
    grad = 1.0
    val = float(x)
    for func in reversed(functions):
     forward_fn, deriv_fn = ops[func]   # Direct O(1) lookup — no match needed!
     grad *= deriv_fn(val)
     val = forward_fn(val)
    return float(grad)