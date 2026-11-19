def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.
    rowA = len(a)
    rowB = len(b)
    if rowA != rowB:
        return -1
    result = [0 for _ in range(rowA)]
    for i in range(rowA):
        result[i] += a[i] + b[i]
    return result 
    pass