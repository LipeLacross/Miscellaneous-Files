'''
Exemplo 2: Modifique o programa anterior para que 
ele funcione para qualquer número, mas exatamente 10 vezes.
'''
qt_vezes = 0

while (qt_vezes < 10):
    #leitura do número
    numero = int(input("Digite um número (se num < 0, programa encerra): "))

    # processamento para saber se o número é par ou ímpar
    if (numero % 2 == 0):
       print("Número informado é par.")
    else:
       print("Número informado é ímpar.")

    #atualizar a variavel da condição
    qt_vezes += 1

print("Fim do programa")