def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    # Your code here
    expected_value = float((n+1)/2)
    variance = float((n**2 - 1)/12)
    return (expected_value,variance)
    pass