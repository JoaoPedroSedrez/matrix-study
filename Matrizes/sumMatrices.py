matrixA = [[-10,1,4,6],
           [2,3,2,8]]

matrixB = [[1,8,4,-1],
           [0,6,3,-3]]

matrixC = [[0,0,0,0],
           [0,0,0,0]]


for i in range(len(matrixA)):
    for j in range(len(matrixA[0])):  
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]


for row in matrixC:
    print(row)
