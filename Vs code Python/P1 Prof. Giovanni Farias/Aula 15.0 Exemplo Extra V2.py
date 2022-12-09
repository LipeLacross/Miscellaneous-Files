#gerar uma sequência ordenada
sequencia = []
for i in range(1200):
  sequencia.append((i + 1) * 10)

print(sequencia)

valor = int(input("Qual valor você quer buscar na sequência? "))

print("---------------------")

# implementar busca linear pelo índice da sequência com for
contador1 = 0
for i in range(len(sequencia)):
    contador1 = contador1 + 1  
    if sequencia[i] == valor:
        print("Valor encontrado!")
        break

if i != valor:
    print("Valor inexistente!")

print("Com for percorrendo os índices da sequencia, trecho de código repete:", contador1)

print("---------------------")
