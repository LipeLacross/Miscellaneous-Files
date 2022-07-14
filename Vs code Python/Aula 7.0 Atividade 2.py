# Escreva um programa que receba como entrada um número 
# e exiba uma mensagem informando se ele é par ou ímpar.
# Lembrete: Um número é par se for divisível por dois, ou seja, 
# se na divisão inteira por dois o resto for zero. Caso contrário, ele será ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")