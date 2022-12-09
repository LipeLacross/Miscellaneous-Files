#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for i in range(5):
    num = int(input("Digite um número: "))
    soma = soma + num

media = soma/5
print(soma)
print(media)