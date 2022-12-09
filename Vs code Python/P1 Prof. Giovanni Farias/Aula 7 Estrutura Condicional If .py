'''
Comando if... then... else

    -Sintaxe:
	if <variável> <condição>:
	    corpo do if
	else:
	    corpo do else
	instrução seguinte n

     - Também é possível usar o if sem o else!

Comando if... then... else... mais genérico

    -Sintaxe:
	if <variável> <condição>:
	    corpo 1
	elif <variável> <condição>:
	    corpo 2
    elif <variável> <condição>:
	    corpo3
	...
	else:
	    corpo do else

Múltiplos if vs if... then... else mais genérico
'''
print("Digite a primeria nota: ")
nota1 = float(input())

print("Digite a segunda nota: ")
nota2 = float(input())

media = (nota1 + nota2)/2

print("A média obtida foi:", media)

if media >= 7 :
    print("Aluno aprovado! Parabéns!")
elif media >= 3 :
    print("Aluno está na final! Estude!")
else:
    print("Aluno foi reprovado! Fica para próxima!")

print("Fim do programa!")