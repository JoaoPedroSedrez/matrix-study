# Prompt the user to input a number to generate an identity matrix
a = int(input('Insira um número para gerarmos uma matriz identidade: '))

# Initialize an empty list to hold the identity matrix
matrizInicial = []

# Loop through the range of the input number to create each row
for i in range(a):
    # Create a row filled with zeros
    row = [0] * a

    # Set the diagonal element to 1 for the identity matrix
    row[i] = 1

    # Append the row to the identity matrix
    matrizInicial.append(row)

# Print each row of the identity matrix
for row in matrizInicial:
    print(row)
