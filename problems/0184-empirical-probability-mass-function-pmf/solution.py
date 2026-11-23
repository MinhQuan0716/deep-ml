from collections import Counter
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    counts = Counter(samples)
    total = sum(counts.values())
    if total == 0:
        return []
    return [(value, count / total) for value, count in sorted(counts.items())]