def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Your code here
    n_features = len(vectors)
    N = len(vectors[0])
    means = [sum(row) / N for row in vectors]
    centered = [[(x - mean) for x in row ] for (row,mean) in zip(vectors,means)]
    cov = [[0.0] * n_features for _ in range(n_features)]
    for i in range(n_features):
        for j in range(n_features):
          cov[i][j] = sum(a * b for a, b in zip(centered[i], centered[j])) / (N - 1)
    return cov