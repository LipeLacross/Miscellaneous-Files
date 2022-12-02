'''
Exemplo 1: Escreva um programa que receba como entrada vários números, 
até que seja informado um número negativo, e informe se cada um deles é par ou ímpar. 
'''
# leitura inicial do numero
numero = int(input("Digite um número (se num < 0, programa encerra): "))

if numero < 0:
    print("==Número inválido==")
else:
    while (numero >= 0):
        # processamento para saber se o número é par ou ímpar
        if (numero % 2 == 0):
            print("Número informado é par.")
        else:
            print("Número informado é ímpar.")

        #atualizar a variável da condição
        numero = int(input("Digite um número (se num < 0, programa encerra): "))
        if numero < 0:
            print("==Número inválido==")
        

print("==Fim do programa==")