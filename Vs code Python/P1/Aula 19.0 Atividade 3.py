'''
Escreva um programa para receber como entrada 10 números informados pelo usuário. 
Em seguida, usando as funções testaMultiplo4 e testaDivisor já desenvolvidas, 
o programa deve exibir a quantidade de múltiplos de 4 e 
a soma dos divisores de 300 dentre os números informados.
'''
def testaMultiplo4(numero):
    if numero % 4 == 0:
        return True
    else:
        return False

def testaDivisor(numero1, numero2):
    if numero1 % numero2 == 0:
        return True
    else: 
        return False

qtdMultiplos4 = 0
somaDivisor300 = 0

for i in range(10):
    numero = int(input("Digite um número: "))

    if testaMultiplo4(numero): # se for true aciona os comandos do if
        qtdMultiplos4 += 1 # equivale a qtdMultiplos4 = qtdMultiplos4 + 1
    
    if testaDivisor(300, numero):
        somaDivisor300 += numero

print("Quantidade de múltiplos de 4:", qtdMultiplos4)
print("Soma dos divisores de 300:", somaDivisor300)