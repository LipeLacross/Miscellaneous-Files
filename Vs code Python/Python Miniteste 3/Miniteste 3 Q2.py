import random

print("==Bem-vindo==")
print("==Este é o somador de 2 listas==")

lista1 = []
lista2 = []
lista3 = []

resposta = int(input("Quer fazer as listas? Digite 1 para sim e 2 para não: "))


if resposta == 1:
    contador = 1
    for i in range(10):
        num1 = int(input("Digite o " + str(contador) + "º número da primeira lista: "))
        lista1.append(num1)
        contador += 1
    
    contador = 1
    for i in range(10):
        num2 = int(input("Digite o " + str(contador) + "º número da segunda lista: "))
        lista1.append(num2)
        contador += 1
    
    for i in range(10):
        lista3.append(lista1[i])
        lista3.append(lista2[i]) 
    
    print(lista1)
    print(lista2)
    print(lista3)     
elif resposta == 2:
    for i in range(10):
        num1 = random.randint(0, 100)
        lista1.append(num1)
        
    for i in range(10):
        num2 = random.randint(0, 100)
        lista2.append(num2)

    for i in range(10):
        lista3.append(lista1[i])
        lista3.append(lista2[i])

    print(lista1)
    print(lista2)
    print(lista3)
else:
    print("Número inválido, fim do programa.")