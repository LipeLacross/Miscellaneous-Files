# Calculadora de IMC que Felipe fez
print('================Vamos calcular seu imc================')

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Qual a sua altura em cm? ')) / 100

imc = peso / altura ** 2

print('Seu imc é:', imc)

if imc < 18.5:
    print('Magreza')
elif imc > 18.5 and imc < 24.9:
    print('Normal')
elif imc > 24.9 and imc < 30:
    print('Sobrepeso')
else:
    print('Obesidade')


