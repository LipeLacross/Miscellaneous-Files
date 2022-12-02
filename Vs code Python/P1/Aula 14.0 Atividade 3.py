# programa lê 20 números
# e exibir a soma dos pares

cont = 0
soma = 0
while cont < 20:
    num = int(input("Digite um número:"))
    cont += 1
    if num % 2 == 0:
        soma += num
print("Soma dos números pares:", soma)