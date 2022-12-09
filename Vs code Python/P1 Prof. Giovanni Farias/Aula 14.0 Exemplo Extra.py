#Para criar uma sequência com uma quantidade variável de números  
sequencia = []

while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    else:
        sequencia.append(num)

print(sequencia)
