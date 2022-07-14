'''
Exemplo 3: Desenvolva um programa que calcula 
e imprime uma sequência de potências de 2, para os 
números entre dois números dados. Contudo, ao invés de tratar 
todos os números no intervalo, a cada iteração o programa pula um número. 
Ao final, imprima quantas potências foram calculadas.
'''
print("Potências de 2 em 2 de I a F")

i = int(input("Digite o inicio do intervalo (i): "))
f = int(input("Digite o inicio do intervalo (f): "))

numero = i

while (numero < f):
    potencia = numero ** 2
    print(numero, potencia)
    numero += 2