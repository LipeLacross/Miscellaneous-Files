#gerar uma sequência ordenada
sequencia = []
for i in range(1200):
  sequencia.append((i + 1) * 10)

print(sequencia)

valor = int(input("Qual valor você quer buscar na sequência? "))

print("---------------------")
# implementar busca linear com for
contador = 0
for i in sequencia:
    contador = contador + 1  
    if i == valor:
        print("Valor encontrado!")
        break

if i != valor:
    print("Valor inexistente!")

print("Com for percorrendo os valores da sequencia, trecho de código repete:", contador)

print("---------------------")