# Faça um Programa que recebe um número e o percentual desejado, e 
# produz como saída o percentual do número desejado.
print('======Percentual de um número======')

numero = float(input('Digite um número: '))
porcentagem = float(input('Percentual você quer: '))

porcentagem = porcentagem/100

resultado = numero * porcentagem

print('O resultado é', resultado)