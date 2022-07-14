# Faça um programa que leia uma sequência de 10 números inteiros e 
# mostre-os na ordem inversa da leitura

sequencia = []
for i in range(10):
    num = int(input("Digite um número: "))
    sequencia.append(num)

print(sequencia)

seqInversa = []
for i in range(len(sequencia) -1, -1, -1):
    seqInversa.append(sequencia[i])

print(seqInversa)
