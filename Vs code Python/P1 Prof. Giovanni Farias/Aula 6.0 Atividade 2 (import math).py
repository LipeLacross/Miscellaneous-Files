# Faça um Programa que peça o raio de um círculo, calcule e imprima sua área.
# area = pi.raio*raio

import math #para funcionar a função pow

print('##Área de um círculo##')

raio = float(input('Digite o raio: '))

#area = 3.14 * raio ** 2 #versão sem o uso da biblioteca math  

area = 3.14 * math.pow(raio, 2) # raio elevado a 2

print('Área é:', area)