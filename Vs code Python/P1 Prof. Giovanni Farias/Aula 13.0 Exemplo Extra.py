#Uso do comando para criar uma sequência de 5 números
sequencia = []
i = 0

while i < 5:
    num = int(input("Digite um número: "))
    sequencia.append(num)
    i += 1

print(sequencia)

'''#Para criar uma sequência determinada pelo usuário
sequencia = []
num = int(input("Digite um número: "))

while num >= 0:
    sequencia.append(num)
    num = int(input("Digite um número: "))

print(sequencia)

'''