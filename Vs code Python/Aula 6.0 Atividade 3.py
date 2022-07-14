# Faça um Programa que recebe um tempo em dias, horas e minutos, e
# produz como saída esse tempo total em minutos
print('======Programa de conversão em minutos======')

dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))

dias = dias * 24 * 60 
horas = horas * 60 

resultado = dias + horas + minutos

print('minutos:', resultado)