# Faça um programa que leia 5 números e informe o maior número.

maior = int(input("Digite um número: "))
menor = maior
for i in range(4):
    num = int(input("Digite um número: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    
print(maior)
print(menor)