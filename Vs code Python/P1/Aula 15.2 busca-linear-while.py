'''
- Linear: a chave é procurada linearmente ao longo dos elementos da estrutura de dados 
(por exemplo, de uma lista) até que o elemento seja encontrado.
'''
lista = [80, 70, 10, 100, 90, 60, 40, 50]

chave = int(input("Qual o número a ser buscado? "))
chave_encontrada = False
qt_repeticoes = 0

indice = 0
while (indice < len(lista)):
    qt_repeticoes += 1  # qt_repeticoes = qt_repeticoes + 1
    if (chave == lista[indice]):
        chave_encontrada = True
        break
    indice += 1 # indice = indice + 1

if (chave_encontrada):
    print("O número foi encontrado.")
else:
    print("O número NÃO foi encontrado.")

print("Quantidade de reptições: ", qt_repeticoes)