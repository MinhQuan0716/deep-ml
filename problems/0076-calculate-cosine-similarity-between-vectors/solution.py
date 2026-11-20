import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    result = 0
   
    if(v1.shape!=v2.shape or v1.size == 0 or v2.size == 0) :
        raise ValueError
    else:
        v1_magnitude = np.sqrt(np.sum(np.power(v1,2))) 
        v2_magnitude  = np.sqrt(np.sum(np.power(v2,2)))
        if (v1_magnitude == 0 or v2_magnitude == 0):
            raise ValueError
        result = float(np.divide(np.dot(v1,v2),v1_magnitude  * v2_magnitude))
    return result