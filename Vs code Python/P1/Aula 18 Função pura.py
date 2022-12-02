
def num_pares(lista):
    resposta = []
    
    for num in lista:
        if (num % 2 == 0):
            resposta.append(num)

    return resposta


lista = [10, 3, 6, 7, 9, 11, 22]

assert num_pares(lista) == [10, 6, 22]
assert lista == [10, 3, 6, 7, 9, 11, 22]
assert num_pares([]) == []

print(type(num_pares(lista))) #Tipo lista

print(num_pares(lista)) #Tem retorno

print(lista)
