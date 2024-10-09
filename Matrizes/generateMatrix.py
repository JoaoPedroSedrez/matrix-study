# Initialize a 2x4 matrix filled with zeros
matrizX = [[0, 0, 0, 0], 
           [0, 0, 0, 0]]

# Loop through each row of the matrix
for x in range(0, len(matrizX)):
    # Loop through each column in the current row
    for i in range(len(matrizX[x])):
        # Prompt the user to input a number for the current position in the matrix
        matrizX[x][i] = input('Insira um número: ')

# Print each row of the filled matrix
for row in matrizX:
    print(row)
