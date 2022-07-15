array_not_repetition = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
array = [[10, 20, 30], [10, 30, 60], [20, 80, 90]]


def check_repeated_elements(matriz):
    verify = False
    for om, m in enumerate(matriz):
        for x in m:
            for of, f in enumerate(matriz):
                if of > om:
                    if x in matriz[of]:
                        verify = True
                        break
    return verify


assert not check_repeated_elements(array_not_repetition)
assert check_repeated_elements(array)

print(f'Arrays without repetitions: {check_repeated_elements(array_not_repetition)}')
print(f'Arrays with repetitions: {check_repeated_elements(array)}')

# L7: om = index da matriz | m = valor da matriz
# L8: x = valores da matriz[?]
# L9: of = index da matriz | f = valor da matriz
# L10: se o index de matriz é maior index da matriz do primeiro laço, passa verificação, isso evita de verificar vetores já verificados
# L11: verifica se o elemento (x) existe nos vetores que não são seu local, caso encontre altera a variavém verify e ativa o break, visto que já chegou a um resultado desejado independente da posição em que foi encontrado.

# Os asserts devem ser essenciais em testes

# parece que ainda dá pra melhorar essa lógica, deixar o cógido menor e com mais performance 