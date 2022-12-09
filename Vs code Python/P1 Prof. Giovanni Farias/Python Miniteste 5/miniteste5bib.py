def calculaComissao(abadas):
    comissao = abadas * 5.6
    return comissao

def calculaBonus(abadas):
    if abadas > 50:
        bonus = 70
    else:
        bonus = 0
    return bonus

def obtemMaior(lista):
    contador = 0
    for i in lista:
        if i > contador:
            contador = i
        else:
            continue
    return contador

def obtemMenor(lista):
    contador = 10000000000000000000000000000000000000 
    for i in lista:
        if i < contador:
            contador = i
        else:
            continue
    return contador

