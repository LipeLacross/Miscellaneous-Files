nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
frequencia = float(input("Digite o percentual de frequência (0 a 100): "))

reprovadoPorFalta = frequencia < 75

if reprovadoPorFalta:
    print("Aluno reprovado por falta!")
else:  
    media = (nota1+nota2) / 2
    if media >= 7:
        print("Aluno aprovado!")
    elif media >= 3:
        print("Aluno está na final!")
    else:
        print("Aluno reprovado por nota!")