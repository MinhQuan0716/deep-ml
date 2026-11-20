def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
   
    rowA = len(a)
    colA = len(a[0])
    rowB = len(b)
    colB = len(b[0])
    if(colA != rowB):
        return -1
    c = [[0 for j in range(colB)] for i in range(rowA)]
    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                c[i][j] += a[i][k] * b[k][j]
    return c