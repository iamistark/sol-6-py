def multiply(mat1, mat2):
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            temp = 0
            for x in range(k):
                temp += mat1[i][x] * mat2[x][j]
            result[i][j] = temp

    return result
