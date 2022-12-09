'''
Instrução For

   - permite executar repetidamente um certo número de vezes um determinado bloco de código.
   - repetição controlada através da iteração de elementos de uma sequencia

   - Sintaxe:
	for <variável> in <sequencia>:
      corpo do for

Função range
   - a função range é utilizada para gerar uma sequência numérica dentro de um intervalo determinado
   - range(fim)
   - range(inicio, fim)
   - range(inicio, fim, incremento)
   '''
print(list(range(5))) #[0, 1, 2, 3, 4] #Para fazer uma sequência de lista
print(list(range(5, 10))) #[5, 6, 7, 8, 9]
print(list(range(5, 10, 2))) #[5, 7, 9] 
print(tuple(range(5))) #Para fazer uma sequência de tuplo
print(tuple(range(5, 10)))
print(tuple(range(5, 10, 2)))

numeros = []

QuantidadeDeNumeros = int(input("Quantos números você quer verificar? "))
#A função range é utilizada para gerar uma sequência numérica dentro de um intervalo determinado
for i in range(QuantidadeDeNumeros): #Vai criar uma sequência de 0 até o número digitado - 1 
   num = int(input("Qual o número a ser verificado? "))
   numeros.append(num)

print("Números: ", numeros)

for u in numeros: #Semântica: para cada variável nessa sequência execute isso.
   if (u % 3 == 0):
      print(u, "é divisível por 3.")


contador = 0
for num_atual in numeros:
   if (num_atual % 3 == 0):
      contador = contador + 1

print(contador, " números foram divisíveis por 3.") 
