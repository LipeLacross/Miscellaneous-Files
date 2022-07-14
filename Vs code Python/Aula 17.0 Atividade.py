''' #Questão 3 da lista 5
Escreva uma função testaMultiplo4 que receba por parâmetro um número 
inteiro e retorne verdadeiro se ele for múltiplo de 4, ou falso caso contrário. 
Um número é múltiplo de 4 quando o resto de sua divisão por 4 for zero. 
Segue tabela com exemplo de parâmetro e valor esperado como retorno.
Parâmetro Retorno
4          True
7          False
-16        True
-7         False
'''

def testaMultiplo4(numero):
    if numero % 4 == 0:
        return True
    else:
        return False

# Testando função testaMultiplo4 usando o print
print(testaMultiplo4(4))
print(testaMultiplo4(7))
print(testaMultiplo4(-16))
print(testaMultiplo4(-7))

'''#Questão 4 da lista 5
Escreva uma função testaDivisor que receba como parâmetro dois números inteiros, 
e retorne verdadeiro caso o segundo seja divisor do primeiro, ou falso caso contrário.
Parâmetro Retorno
3    1     True
6    18    False
18   6     True
14   4     False
'''
def testaDivisor(num1, num2):
    if num1 % num2 == 0:
        return True
    else: 
        return False

# Testando função testaDivisor usando o assert
assert testaDivisor(3, 1)
assert not testaDivisor(6, 18)
assert testaDivisor(18, 6)
assert not testaDivisor(14, 4)

'''#PROGRAMA DA QUESTÃO 5
Escreva um programa para receber como entrada 10 números informados pelo usuário. 
Em seguida, usando as funções testaMultiplo4 e testaDivisor já desenvolvidas, 
o programa deve exibir a quantidade de múltiplos de 4 e a soma dos divisores 
de 300 dentre os números informados.
'''
qtdMultiplos4 = 0
somaDivisores300 = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    if testaMultiplo4(numero):
        qtdMultiplos4 += 1

    if testaDivisor(300, numero):
        somaDivisores300 += numero

print("Múltiplos de 4:", qtdMultiplos4)
print("Soma dos divisores de 300:", somaDivisores300)
