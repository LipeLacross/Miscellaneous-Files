'''
  - slicing 
	- permite recuperar uma subsequência pelos índices (inicial:fim+1)
	- NÃO RECOMENDADA neste disciplina por não ser um comando disponível em todas as linguagens 
	- produz nova sequência sem alterar a seq original
'''
#Slicing funciona com strings, listas e tuplas.
#Ex com string
nome2 = 'Pedro corno da silva'
print(len(nome2))
print(nome2[0:5])
print(nome2[6:11])
print(nome2[6:])# Mesma coisa que print(nome2[6:20])
print(nome2[:6])# Mesma coisa que print(nome2[0:6])
