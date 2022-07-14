numeros = []

num1 = int(input("Qual o número a ser verificado? "))
numeros.append(num1)
num2 = int(input("Qual o número a ser verificado? "))
numeros.append(num2)
num3 = int(input("Qual o número a ser verificado? "))
numeros.append(num3)

print("Números:", numeros)

if (numeros[0] % 3 == 0):
    print(numeros[0], "é divisível por 3")


if (numeros[1] % 3 == 0):
    print(numeros[1], "é divisível por 3")


if (numeros[2] % 3 == 0):
    print(numeros[2], "é divisível por 3")
