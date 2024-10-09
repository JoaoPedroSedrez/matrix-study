


# ex4
a = int(input('Insira um número para gerarmos uma matriz identidade: '))


matrizInicial = []
for i in range(a):
  
    row = [0] * a

    row[i] = 1
    matrizInicial.append(row)

for row in matrizInicial:
    print(row)

