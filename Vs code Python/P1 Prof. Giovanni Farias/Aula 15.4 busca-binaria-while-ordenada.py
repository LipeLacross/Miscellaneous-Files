'''
- Binária: usa o paradigma de divisão e conquista, diminuindo espaço de busca. 
A ideia é comparar o elemento buscado sempre com o meio da sequência. 
'''
#lista = [10, 20, 30, 40, 50, 60, 70, 80]

lista = []
for i in range(10, 1001, 10):
    lista.append(i)

print("O tamanho da lista é:", len(lista))

chave = int(input("Qual o número a ser buscado? "))
chave_encontrada = False
qt_repeticoes = 0

i_inferior = 0
i_superior = len(lista) -1

while (i_inferior <= i_superior):
    qt_repeticoes += 1
    meio = (i_inferior + i_superior) // 2 #é necessário somar a posição do primeiro do número com a posição do último número e dividir por 2
    if (chave == lista[meio]):
        chave_encontrada = True
        break
    elif (chave > lista[meio]):
        i_inferior = meio + 1
    else: 
        i_superior = meio - 1


if (chave_encontrada):
    print("O número foi encontrado.")
else:
    print("O número NÃO foi encontrado.")

print("Quantidade de repetições:", qt_repeticoes)