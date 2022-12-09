print('================Vamos calcular seu imc================')

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Qual a sua altura? '))
imc = peso / altura ** 2

print('Seu imc é:', imc)
