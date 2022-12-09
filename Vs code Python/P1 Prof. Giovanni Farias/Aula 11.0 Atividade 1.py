# Faça um programa que leia uma sequência de 5 números inteiros e mostre-os

qtd = int(input("Quantas vezes você quer informar um número? "))

sequencia = []

for i in range(qtd):
    msg = "Digite "+ str(i + 1) +"º número: "
    num = int(input(msg)) #O texto do msg é printado e uma resposta é solicitada
    sequencia.append(num)

print(sequencia)