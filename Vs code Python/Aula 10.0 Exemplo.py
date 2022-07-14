listaInt = [20, 5, 4, 31, 77, 85, 40, 21]

for valor in listaInt:
    if valor % 2 == 0:
        print(valor)

print("-----------")
for i in range(len(listaInt)): #Vai criar uma sequência de
    if listaInt[i] % 2 == 0:
        print(i)
        break

print("-----------")
for i in range(len(listaInt)):
    print(i, listaInt[i])

print("-----------")
for i in range(len(listaInt) -1, -1, -1):
    print(i, listaInt[i])

print("-----------")
for i in range(len(listaInt)):
    if listaInt[i] % 2 == 0:
        print(i)
        break

print("-----------")
contaPares = 0
for i in range(len(listaInt)):
    if listaInt[i] % 2 == 0:
        contaPares = contaPares + 1

print("Existem", contaPares, "númeors pares na lista")

print("-----------")
acumulaPares = 0;
for i in range(len(listaInt)):
    if listaInt[i] % 2 == 0:
        acumulaPares = acumulaPares + listaInt[i]

print("A soma dos pares resulta em", acumulaPares)
    