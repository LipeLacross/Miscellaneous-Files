'''
- Nova função:
 	- Sintaxe
 	    - def nome_funcao(arg1, arg2, ..., argn):
		    corpo da função
		    return <variavel_resposta>def soma(op1, op2):
        print("Dentro da função")
        resultado = op1 + op2
        return resultado
'''
def soma(op1, op2):
    print("Dentro da função")
    resultado = op1 + op2
    return resultado

print("Começo do programa")
calculo = soma(2, 3)
print(calculo)

calculo2 = soma(10, 20)
print(calculo2)

calculo3 = soma(50, 50)
print(calculo3)

print("Fim do programa!")
