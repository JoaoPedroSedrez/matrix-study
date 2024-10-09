# Define matrix A (2x4)
matrixA = [[-10, 1, 4, 6],
            [2, 3, 2, 8]]

# Define matrix B (2x4)
matrixB = [[1, 8, 4, -1],
            [0, 6, 3, -3]]

# Initialize matrix C (2x4) to store the result of the addition
matrixC = [[0, 0, 0, 0],
            [0, 0, 0, 0]]

# Loop through each row of matrix A
for i in range(len(matrixA)):
    # Loop through each column of matrix A (and matrix B, since they have the same shape)
    for j in range(len(matrixA[0])):  
        # Add corresponding elements of matrix A and matrix B, storing the result in matrix C
        matrixC[i][j] = matrixA[i][j] + matrixB[i][j]

# Print each row of the resulting matrix C
for row in matrixC:
    print(row)
