# função pura
from ast import If


def encontraNome(nome, listaNomes):
    for umNome in listaNomes:
        if str(nome).lower() == str(umNome).lower():
            return True
    return False

# função com efeito colateral
def adicionaNome(nome, listaNomes):
    listaNomes.append(nome)
    return

# função com efeito colateral e retorno
def removeNome(nome, listaNomes):
    indice = -1
    for i in range(len(listaNomes)):
        if str(nome).lower() == str(listaNomes[i]).lower():
            indice = i
            break

    if indice != -1:
        return listaNomes.pop(indice)
    else:
        return None
