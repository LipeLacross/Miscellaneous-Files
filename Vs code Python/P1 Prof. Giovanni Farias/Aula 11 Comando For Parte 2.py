import random #Para usar o ramdom.randit()

numeros = []

qt_numeros = int(input("Qual o tamanho da sequência a ser gerada? "))

for i in range(qt_numeros):
    num = random.randint(0, 10) #Vai gerar um número entre 0 e 10
    numeros.append(num)

print("Números: ", numeros)

contador = 0
for num_atual in numeros:
    if (num_atual % 3 == 0):
        contador = contador + 1

print(contador, " números foram divisíveis por 3.")