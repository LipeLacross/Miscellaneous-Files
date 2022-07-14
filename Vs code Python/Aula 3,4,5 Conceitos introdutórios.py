
'''
 - Variáveis
   - podem ter o nome iniciado por _ ou caracteres, seguidos de digitos, letras e _
   - Case sensitive- Diferencia maiúsculas e minúsculas
   - Dinamicamente tipificadas

 - Atribuição
   - Ordem das atribuições é importante na definição de expressões
   - Só variáveis já definidas podem ser usadas

 - Expressões
   - Ordem de precedência: **; * /; + -
   - podemos usar parenteses para redefinir as precedências
  
''' 
gordo1 = int(5.5) #pode ser convertido para outro tipo de dado: gordo1 = float(5.5) 
gordo2 = float(6.5) 
gordo3 = str(7.5)
print(gordo1, gordo2, gordo3) #print() serve para imprimir algo no terminal
print(type(gordo1)) #para saber o tipo de dado
print(type(gordo2))
print(type(gordo3))
print(len(gordo3)) #para saber quantos caracteres tem em uma string

num1 = 2 
num2 = 5
num3 = 7
continha = ((num1 * num2) + num3) / (num3 - num2) #expressão de teste
Total = continha
print(Total - 4)

namorada = 'O'
namorado = 'B'
print(namorado, namorada)

prisão = namorado + namorada #soma de caracteres (concatenação)

print(prisão + ' para o corno')
print (prisão * 4) #repetição da palavra

print('God') #para imprimir uma string de forma direta
print(444.5) #imprime números de forma direta

