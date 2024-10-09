# Define matrix A (2x3)
matrixA = [[2, 3, 1],
            [-1, 0, 2]]

# Define matrix B (3x2)
matrixB = [[1, -2],
            [0, 5],
            [4, 1]]

# Initialize the result matrix (2x2) with zeros
result = [[0, 0],
          [0, 0]]

# Loop through each row of matrix A
for i in range(len(matrixA)):
    # Loop through each column of matrix B
    for j in range(len(matrixB[0])):
        # Loop through each element in the current row of matrix A
        # and the current column of matrix B
        for k in range(len(matrixB)):
            # Perform the multiplication and add to the result matrix
            result[i][j] += matrixA[i][k] * matrixB[k][j]

# Print each row of the result matrix
for row in result:
    print(row)
