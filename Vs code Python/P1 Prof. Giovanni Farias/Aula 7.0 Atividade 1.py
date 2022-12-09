# Escreva um programa que receba como entrada um número 
# e exiba uma mensagem informando se ele é positivo, negativo ou neutro.
# Lembrete: Os números maiores que zero são chamados de positivos, 
# enquanto os números menores que zero são os negativos. Zero é um número neutro.

numero = float(input("Digite um número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Neutro")