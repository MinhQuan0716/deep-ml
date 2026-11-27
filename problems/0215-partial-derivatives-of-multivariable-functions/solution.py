import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
    """
    Compute partial derivatives of multivariable functions.
    
    Args:
        func_name: Function identifier
            'poly2d': f(x,y) = x²y + xy²
            'exp_sum': f(x,y) = e^(x+y)
            'product_sin': f(x,y) = x·sin(y)
            'poly3d': f(x,y,z) = x²y + yz²
            'squared_error': f(x,y) = (x-y)²
        point: Point (x, y) or (x, y, z) at which to evaluate
    
    Returns:
        Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
    """
    # Your code here
    match func_name:
        case 'poly2d':
            (x,y) = point
            df_x = 2*x*y+y**2
            df_y = x**2+2*x*y 
            return (float(df_x),float(df_y))
        case 'exp_sum':
            (x,y) = point
            df_x = np.e**(x+y)
            return (float(df_x),float(df_x))
        case 'product_sin':
            (x,y) = point
            df_x = np.sin(y)
            df_y = x*np.cos(y)
            return (float(df_x),float(df_y))
        case 'poly3d':
            (x,y,z) = point
            df_x = 2*x*y
            df_y = x**2+ z**2
            df_z =  2*y*z
            return (float(df_x),float(df_y),float(df_z))
        case 'squared_error':
            (x,y) = point
            df_x = 2*(x-y)
            df_y = -2*(x-y)
            return (float(df_x),float(df_y))
        case _:
            raise ValueError(f"Unknown function: {func_name}")
    pass