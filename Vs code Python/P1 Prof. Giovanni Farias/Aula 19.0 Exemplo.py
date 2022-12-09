import Aula19BibExemplo

listaNomes = ["Paulo", "Maria", "João", "Ana"]
nomeParaEncontrar = "José"

print(listaNomes)

assert Aula19BibExemplo.encontraNome(nomeParaEncontrar, listaNomes) == False
# O de cima faz o mesmo que o de baixo
assert not Aula19BibExemplo.encontraNome(nomeParaEncontrar, listaNomes)


assert Aula19BibExemplo.encontraNome("Paulo", listaNomes)
assert Aula19BibExemplo.encontraNome("Ana", listaNomes)
assert Aula19BibExemplo.encontraNome("ana", listaNomes)
assert Aula19BibExemplo.encontraNome("ANA", listaNomes)

print(listaNomes)

Aula19BibExemplo.adicionaNome("Carlos", listaNomes)

print(listaNomes)

assert Aula19BibExemplo.removeNome("Maria", listaNomes) == "Maria"
print(listaNomes)