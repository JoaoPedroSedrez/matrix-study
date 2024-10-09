matrixA = [[2, 3 ,1],
           [-1, 0 ,2]]

matrixB = [[1, -2],
           [0 , 5],
           [4,1]]

result = [[0,0],
          [0,0]]


for i in range(len(matrixA)):
    for j in range(len(matrixB[0])):
        for k in range(len(matrixB)):
            result[i][j] += matrixA[i][k] * matrixB[k][j]

for row in result:
    print(row)