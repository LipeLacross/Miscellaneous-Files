lista = []

while True:
    numeros = int(input("Digite um número positivo, se for negativo o programa encerra: "))
    if numeros % 3 == 0:
        lista.append(numeros)
    if numeros < 0:
        print("Número negativo!")
        break
print(lista, "São múltiplos de 3!")
print("==Fim do programa==")
