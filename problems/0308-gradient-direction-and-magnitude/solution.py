import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    
    Args:
        gradient: A list representing the gradient vector
    
    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    # Your code here
    magnitude = np.float64(np.sqrt(np.sum(np.power(gradient,2))))
    direction = []
    descent_direction = []
    for i in range(len(gradient)):
        pos_direction = float(gradient[i]/magnitude)
        if(gradient[i] == 0):
            pos_direction = 0.0
        direction.append(pos_direction)
        descent_direction.append(-pos_direction)
    result = {
        "magnitude": magnitude,
        "direction": direction,
        "descent_direction": descent_direction
    }
    return result