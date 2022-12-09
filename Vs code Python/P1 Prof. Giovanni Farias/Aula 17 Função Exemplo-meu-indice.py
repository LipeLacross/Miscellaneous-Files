def meu_indice(lista, chave):
    for indice in range(len(lista)):
        if (lista[indice] == chave):
            return indice
    return -1 
    

lista_inteiros = [10, 20, 30, 40, 50, 60]

assert meu_indice(lista_inteiros, 30) == 2 #Vai verificar se a expressão é True, se não for True dá error
assert meu_indice(lista_inteiros, 10) == 0 
assert meu_indice(lista_inteiros, 100) == -1