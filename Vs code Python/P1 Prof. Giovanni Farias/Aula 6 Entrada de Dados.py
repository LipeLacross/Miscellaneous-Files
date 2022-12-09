'''
   - Saída
      - print(<expressão>)
      - print(<expressão 1, <expressão 2>, ...<expressão n>)

   - Entrada
      - input()
'''
print('Você vai digitar um número: ')
numero = input() #o input sempre converterá o dados para string

print('Número digitado', numero)

print('Digite um número inteiro: ')
inteiro = int(input()) #especificando o tipo de dado da entrada

print('Observe seu número inteiro:', inteiro)

float = input('Digite um dado tipo float: ') #para que não haja o salto de linha para digitar a resposta
print('Aqui está o dado', float)

#Outro método
mensagem = "Tu é corno? Digite 1 se sim ou digite 2 se não: "
resposta = (int(input(mensagem)))
print(type(resposta))
print(resposta)

