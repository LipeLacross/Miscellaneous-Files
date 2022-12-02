#Sequência de tuplos
'''
  - Tuplas
	- é possível criar uma lista com elementos de diversos tipos
	- imutável
  - operações válidas em sequências
    - indexação
	- permite recuperar um elemento pelo seu índice
	- índices de 0 a n-1 (onde n é o tamanho da sequência)
	- índices também são acessados por números negativos: -n a -1 (onde n é o tamanho da sequência)	
'''   
umaTupla = (10, 20, 30, 40, 50, 'A', True, ('d',1), [1,2])
print(umaTupla)
print(umaTupla[0])
print(umaTupla[7][0])
print(umaTupla[8])
umaTupla[8][0] = 10 #para modificar um elemento de uma lista que está dentro de uma tupla
print(umaTupla[8])
#não é possível modificar, adicionar ou remover elementos por conta da imutabilidade.