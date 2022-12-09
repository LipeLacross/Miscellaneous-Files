# Bubble sort -> criar uma função com dada lista de inteiros 
# para ordenar de forma crescente todos os elementos da lista.Tem efeito colateral??

# (0,1,2,3,4,5)
# [1,3,0,4,5,8]

def ordena_crescente(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i): #-1 para evitar o out of range e i para otimizar o código
            if (lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux


def ordena_decrescente(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if (lista[j] < lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
        

#Crescente
lista = [4,3,1,8,5,0]
print(lista)
print(list(range(len(lista))))
print(range(6))
ordena_crescente(lista)

print(lista)
assert lista == [0,1,3,4,5,8]

#Decrescente
lista_2 = [10,5,100,8,4,2]
print(lista_2)

ordena_decrescente(lista_2)

print(lista_2)
assert lista_2 == [100,10,8,5,4,2]