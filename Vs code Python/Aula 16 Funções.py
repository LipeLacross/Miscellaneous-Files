'''
Funções 
  - Algumas funções que já utilizamos:
	- print()
	- input()
	- range()
	- int()
	- float()
- Essas são exemplos de funções builtin em Pyhton, funções que não precisam de bibliotecas externas

- Função é um trecho de código que é semelhante a um programa em Python, mas com particularidades
    - Não pode ser executada sozinha, precisa ser chamada
    - Permite esconder a implementação do programador, que conhece apenas a interface 
    (nome, parâmetros, retorno)
    - Propõe a solução de um problema específico, ao invés de agrupar várias soluções

- Função pura: aquela que funciona como uma função matemática, com parâmetros e retorno
- Função efeito colateral: aquela função que não tem retorno mas que altera o estado do sistema
- Há funções que possuem retorno e efeito colateral
 
- import - serve para dizer ao interpretador que nosso programa vai 
usar dados ou funções do módulo que está sendo importado

- Nova função:
 	- Sintaxe
 	    - def nome_funcao(arg1, arg2, ..., argn):
		    corpo da função
		    return <variavel_resposta>
'''
print(abs(-10)) #Este comando irá positivar o número.

#Funções de string
nome = 'Micael é corno, corno, e coRNo'
print(nome.lower()) #Fica tudo maiúsculo
print(nome.upper()) #Fica tudo minúsculo
print(nome.count('o')) #Vai contar palavras ou letras
print(nome.find('o')) #Vai procurar uma letra ou palavra e dizer o índice da mesma
print(nome.replace("corno", "cornão")) #Vai substituir uma letra ou palavra por uma letra ou uma palavra
