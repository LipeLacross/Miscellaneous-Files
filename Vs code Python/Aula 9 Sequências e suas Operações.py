'''
Sequências em Python

  - Strings
	- são usadas para lidar com sequência de caracteres
	- imutável
  - Listas
	- é possível criar uma lista com elementos de diversos tipos
	- uma sequência mutável, podemos usar atribuição com índice, append(), pop(), operador +
  - Tuplas
	- imutável
	

  - operações válidas em sequências
    - indexação
	- permite recuperar um elemento pelo seu índice
	- índices de 0 a n-1 (onde n é o tamanho da sequência)
	- índices também são acessados por números negativos: -n a -1 (onde n é o tamanho da sequência)
       
  - slicing 
	- permite recuperar uma subsequência pelos índices (inicial:fim+1)
	- NÃO RECOMENDADA neste disciplina por não ser um comando disponível em todas as linguagens 
	- produz nova sequência sem alterar a seq original
'''
#Sequência de string
nome = 'pica pau'
print(len(nome)) #total de caracteres
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4]) #O "espaço" também é considerado índice
print(nome[5])
print(nome[6])
print(nome[7])
#Com índice negativo #não funciona em todas as linguagens de programação e pode ser problemático
print(nome[-8]) #primeira letra
print(nome[-7])
print(nome[-6])
print(nome[-5])
print(nome[-4]) #O "espaço" também é considerado índice
print(nome[-3])
print(nome[-2])
print(nome[-1]) #Última letra


