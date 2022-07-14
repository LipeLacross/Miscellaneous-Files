def lerMatriz(nLinhas, nColunas):
    mat = []
    for i in range(nLinhas):
        linha = []
        for j in range(nColunas):
            num = int(input("Digite um número:"))
            linha.append(num)

        mat.append(linha)

    return(mat)


def substituirNegativos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < 0:
                matriz[i][j] = 0
    return


def substituirNegativosPura(matriz):
    matMod = []
    for i in range(len(matriz)):
        linhaMod = []
        for j in range(len(matriz[i])):
            if matriz[i][j] < 0:
                linhaMod.append(0)
            else:
                linhaMod.append(matriz[i][j])
        matMod.append(linhaMod)
    return(matMod)      


def somaDiagonal(matriz):
    if len(matriz) > 0 and len(matriz) == len(matriz[0]):
        soma = 0
        for i in range(len(matriz)):
            soma += matriz[i][i]
        return(soma)
    else:
        return None

import bibmatriz

#mat = bibmatriz.lerMatriz(3, 4)
#print("ORIGINAL:", mat)

#matMod = bibmatriz.susbstituirNegativosPura(mat)
#print("ORIGINAL1:", mat)
#print("MODIFICADA:", matMod)

#bibmatriz.substituirNegativos(mat)
#print("ORIGINAL2:", mat)

#Dada uma matriz, qual a soma dos elementos da diagonal principal dessa matriz? Lembrem que a diagonal principal deve ser obtida apenas a partir de uma matriz quadrada.

matriz = bibmatriz.lerMatriz(3, 3)

somaDiagPrincipal = bibmatriz.somaDiagonal(matriz)

print("DIAGONAL:", somaDiagPrincipal)