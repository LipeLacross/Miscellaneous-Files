#Escreva um programa que receba como entrada a quantidade de filhos dos vários funcionários de uma empresa
#até que seja informada uma quantidade negativa
#e exiba a quantidade média de filhos do grupo. 
#(Dica: a média pode ser obtida dividindo-se a soma dos números pela quantidade deles

qtdFuncionarios = 0
totalFilhos = 0

while True:
    qtdFilhos = int(input("Quantos filhos você tem? "))
    if qtdFilhos < 0:
        print("Etapa finalizada!")
        break
    qtdFuncionarios += 1
    totalFilhos += qtdFilhos

media = totalFilhos / qtdFuncionarios
print("A média de filhos por funcionário é:", int(media))

