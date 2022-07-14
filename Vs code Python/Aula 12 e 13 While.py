'''
* Comando while
   - Sintaxe:
	<instruções antes do while>
	while <condição>:
	   corpo do while
	<primeira instrução fora do while>

   - Cuidados ao escrever um comando while
	1) Todas as variáveis testadas na condição precisam ter seus valores iniciais definidos
	
   2) A condição de parada deve ser bem definida para evitar 
   uma quantidade de repetições maior ou menor que a desejada
	
   3) Dentro do corpo do while, é importante que haja pelo menos 
   uma instrução capaz de modificar a condição de parada. 
   Caso contrário, o código será repetido indefinidamente, causando um loop infinito
'''
n = 0

while (n < 100): #Semântica: enquanto for verdadeiro repita
   print("n:", n, " - 2n:", 2*n, " - n**2:", n**2)
   n += 5

print("fim do programa")