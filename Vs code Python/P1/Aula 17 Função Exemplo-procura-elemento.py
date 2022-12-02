def procura_elemento(lista, chave):
    for elem_atual in lista:
        if (elem_atual == chave):
            return True #Se a chave for encontrada retorna true
    return False #Se a chave não for encontrada retorna false


lista_inteiros = [10, 20, 30, 40, 50, 60]

print(procura_elemento(lista_inteiros, 20))
assert procura_elemento(lista_inteiros, 20) #Vai verificar se a expressão é True, se não for True dá error

print(procura_elemento(lista_inteiros, 25))
assert not procura_elemento(lista_inteiros, 25) #Vai verificar se a expressão é False, se não for False dá error
