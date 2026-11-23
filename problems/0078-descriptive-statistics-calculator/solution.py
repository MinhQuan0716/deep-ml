import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    sorted_data = np.sort(data)
    n = len(data)
    mean = float(np.sum(data)/n)
    median = float((sorted_data[(n - 1) // 2] + sorted_data[n // 2]) / 2.0)
    values, counts = np.unique(data, return_counts=True)
    mode = int(values[np.argmax(counts)])
    variance = float((np.sum(np.subtract(data,mean)**2)/n))
    standard_variance = float(np.sqrt(variance))
    quart_percent = np.percentile(data,25)
    half_percent = np.percentile(data,50)
    quarterhalf_percent = np.percentile(data,75)
    iqr = float(quarterhalf_percent - quart_percent)
    result = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_variance,
        "25th_percentile": quart_percent,
        "50th_percentile": half_percent,
        "75th_percentile": quarterhalf_percent,
        "interquartile_range": iqr
    }
    return result
    pass