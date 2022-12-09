# Desenvolva uma função que altere os números da matriz quando eles forem negativos. 
# Nesse caso, todos os números negativos devem ser substituídos por 0.

def eliminaNegativos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 0:
                matriz[i][j] = 'X'
    return



A = [[-1, 0, 5], [4, -9, -6], [1, 5, 8]]
print(A)

eliminaNegativos(A)
print(A)