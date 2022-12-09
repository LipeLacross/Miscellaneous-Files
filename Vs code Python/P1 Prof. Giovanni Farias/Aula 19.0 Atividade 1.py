'''
Escreva uma função testa Multiplo4 que receba por parâmetro um número inteiro e 
retorne verdadeiro se ele for múltiplo de 4, ou falso caso contrário. 
Um número é múltiplo de 4 quando o resto de sua divisão por 4 for zero. 
Segue tabela com exemplo de parâmetro e valor esperado como retorno.

Parâmetro/Valor Retornado

4/True

7/False

-16/True

-7/False
'''
def testaMultiplo4(numero):
    if numero % 4 == 0:
        return True
    else:
        return False

assert testaMultiplo4(4)
assert not testaMultiplo4(7)
assert testaMultiplo4(-16)
assert not testaMultiplo4(-7)