
def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    if len(v) != len(L):
      return 0
    proj = sum(i[0] * i[1] for i in zip(v, L))/ sum(j[0] * j[1] for j in zip(L, L))
    x = [0 for i in range(len(L))]
    for k in range(len(L)):
        x[k] = proj * L[k]
    return x
    pass
