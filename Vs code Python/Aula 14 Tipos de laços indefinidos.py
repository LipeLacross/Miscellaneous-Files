while True:
    # leitura inicial do numero
    numero = int(input("Digite um número (num negativo encerra programa): "))
    if (numero < 0): 
        print("numero foi negativo!")
        break

    # processamento para saber se o número é par ou ímpar
    if (numero % 2 == 0):
        print("Número informado é par.")
    else:
        print("Número informado é ímpar.")

print("Fim do programa")