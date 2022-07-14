numeros = [9, 8, 1, 10, 2, 4, 4, 9, 10, 5, 6, 4, 9, 4, 10, 6, 8, 2, 7, 3]

print("Números: ", numeros)

qt_impares = 0
for indice in range(len(numeros)):
    if (numeros[indice] % 2 != 0):
        qt_impares += 1

print("Existem ", qt_impares, " números ímpares.")


somador = 0
for indice in range(len(numeros)):
    somador += numeros[indice]

print("A soma dos números é ", somador)

media = somador/len(numeros)
print("A média dos números é ", media)

# ---------------------------------------------------

palavra = input("Informe uma palavra: ")
vogais = "aAeEiIoOuU"

contador_vogais = 0
for letra in palavra:
    if (letra in vogais):
        contador_vogais += 1

print("Existem ", contador_vogais, " vogais na setença.")