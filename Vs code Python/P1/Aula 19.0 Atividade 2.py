'''
Escreva uma função testaDivisor que receba como parâmetro dois números inteiros, e 
retorne verdadeiro caso o segundo seja divisor do primeiro, ou falso caso contrário.

Parâmetro/Valor Retornado

3,1/True

6,18/False

18,6/True

14,4/False
'''

def testaDivisor(numero1, numero2):
    if numero1 % numero2 == 0:
        return True
    else: 
        return False

assert testaDivisor(3, 1)
assert not testaDivisor(6, 18)
assert testaDivisor(18, 6)
assert not testaDivisor(14, 4)
