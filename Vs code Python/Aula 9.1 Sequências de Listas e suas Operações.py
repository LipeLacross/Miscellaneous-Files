'''
  - Listas
    - é possível criar uma lista com elementos de diversos tipos
    - uma sequência mutável, podemos usar atribuição com índice, append(), pop(), operador +
  - operações válidas em sequências
    - indexação
	- permite recuperar um elemento pelo seu índice
	- índices de 0 a n-1 (onde n é o tamanho da sequência)
	- índices também são acessados por números negativos: -n a -1 (onde n é o tamanho da sequência)
'''
listaDeInteiros = [10, 20, 30, 40, 50]
print(len(listaDeInteiros))
print(listaDeInteiros[1])

listaDeVogais = ['a', 'b', 'c', 'd', 'e']
print(len(listaDeVogais))
print(listaDeVogais[3])

listaComBooleano = [True, 2 > 2]
print(len(listaComBooleano))
print(listaComBooleano[1])

listaComTudo = [10, 20, 'a', 'b', True, 2 > 2]
print(len(listaComTudo))
print(listaComTudo[1])
print(listaComTudo[3])
print(listaComTudo[5])

listaDeLista = [[10, 20], ['a', 'b'], [True, 2 > 2]]
print(len(listaDeLista))
print(listaDeLista[2]) 
print(listaDeLista[0][0]) #para acessar um indice da lista dentro uma lista
listaDeLista[0][0] = 1000 #para modificar um elemento de uma lista que está dentro uma listaComTudo

#Para modificar algum elemento específico
listaDeInteiros[0] = 100 
print(listaDeInteiros)

#Uso do append
listaDeInteiros.append(60) #Para adicionar algo
print(listaDeInteiros)

#Uso do pop
listaDeInteiros.pop() #Remove o último elemento da lista
print(listaDeInteiros)
listaDeInteiros.pop(0) #Remove o elemento de índice determinado
print(listaDeInteiros)

#Uso do operador +
listMisturada = listaDeInteiros + listaDeVogais
print(listMisturada)

