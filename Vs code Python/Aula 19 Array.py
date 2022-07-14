# Um array é uma lista de inteiros com elementos pré-definidos 
# trocar as posições do primeiro e último elementos da lista
# Num array não é possível modificar uma lista sem usar pop ou append

lista = [1, 2, 3]

print(lista)

aux =  lista[0]
lista[0] = lista[2]
lista[2] = aux

print(lista)

#outra forma de fazer a mesma coisa
lista2 = [4, 5, 6]

print(lista2)

lista2[0], lista2[2] = lista2[2], lista2[0]

print(lista2)