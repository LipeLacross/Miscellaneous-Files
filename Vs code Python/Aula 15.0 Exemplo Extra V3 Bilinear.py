#gerar uma sequência ordenada
sequencia = []
for i in range(1200):
  sequencia.append((i + 1) * 10)

print(sequencia)

valor = int(input("Qual valor você quer buscar na sequência? "))

print("---------------------")

# implementar busca binária
contador2 = 0

inicio = 0 #primeiro índice da sequência
fim = len(sequencia) - 1 #- 1 pois a sequência vai até o índice 1199
print(len(sequencia) - 1)#vai imprimir 1199

while inicio <= fim:
    contador2 = contador2 + 1

    meio = int((inicio + fim) /2)
    if sequencia[meio] == valor:    
        print("Valor encontrado!")
        break
    elif sequencia[meio] < valor:
        inicio = meio + 1
    else:
        fim = meio - 1
    
    print("índice", meio)
    print(print("numero", sequencia[meio]))
    
print("Com busca binária, trecho de código repete:", contador2)