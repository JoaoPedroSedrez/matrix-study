
matrizX = [[0,0,0,0], 
           [0,0,0,0]]

for x in range(0, len(matrizX)):
    for i in range(len(matrizX[x])):
        matrizX[x][i] = input('insira um número: ')

        
for row in matrizX:
    print(row)

    