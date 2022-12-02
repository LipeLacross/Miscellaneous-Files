# Desenvolva uma função que imprime os elementos de uma matriz. 
# Essa função recebe como argumento a matriz a ser impressa e não retorna nada.

def imprimaMatriz(matriz):
    for i in range(len(matriz)):
        linha = ""
        for j in range(len(matriz[i])):
            linha = linha + str(matriz[i][j]) + " "
        print(linha) 
    return

def imprimaColuna(matriz, col):
    for i in range(len(matriz)):
        print(matriz[i][col])
    return


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
imprimaMatriz(A)

print("Coluna do meio")
imprimaColuna(A, 1)
print("Coluna da direita")
imprimaColuna(A, 2)