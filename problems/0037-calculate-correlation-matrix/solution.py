import numpy as np

def calculate_correlation_matrix(X, Y=None):
    # Your code here
    if Y is None: Y = X
    X = np.asarray(X,dtype = float).T
    Y = np.asarray(Y,dtype = float).T
    #Calcualte feature X
    n_features_x = len(X)
    N_x = len(X[0])
    means_x = [sum(row) / N_x for row in X] 
    centered_x = [[(x - mean) for x in row ] for (row,mean) in zip(X,means_x)]
    norms_x = [sum(x * x for x in row) **0.5 for row in centered_x]

    #Calcualte feature Y
    n_features_y = len(Y)
    N_y = len(Y[0])
    means_y = [sum(row) / N_y for row in Y] 
    centered_y = [[(x - mean) for x in row ] for (row,mean) in zip(Y,means_y)]
    norms_y = [sum(x * x for x in row) **0.5 for row in centered_y]

    corr = [[0.0]* n_features_y for  _ in range(n_features_x)]
    for i in range(n_features_x):
        for j in range(n_features_y):
            denom = norms_x[i] * norms_y[j]
            if denom > 0:
             corr[i][j] = float(sum(a * b for a, b in zip(centered_x[i], centered_y[j])) / denom)
    return np.array(corr)
    pass