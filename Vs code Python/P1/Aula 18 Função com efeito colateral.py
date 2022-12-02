def remove_impares(lista):
    
    #Vai ler a lista começando pelo último elemento
    for indice in range(len(lista) - 1, -1, -1): 
        if (lista[indice] % 2 != 0):
            lista.pop(indice) #Remove da lista usando a função pop(indice)


lista = [10, 3, 6, 7, 9, 11, 22]

remove_impares(lista)

assert lista == [10, 6, 22]

print(type(remove_impares(lista))) #Sem classe

print(remove_impares(lista)) #Não retorna nada

