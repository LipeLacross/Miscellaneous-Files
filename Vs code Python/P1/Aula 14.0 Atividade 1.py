#Escreva um programa que receba 
#como entrada números inteiros até que um número maior que 100 seja digitado. 
#Em seguida, esse programa deve exibir a quantidade de números que são pares e positivos.


contadorPar = 0
contadorPositivo = 0
num = 0
while num <= 100:
    num = (int(input("Digite um número: "))) 
    if num % 2 == 0:
        contadorPar += 1
    if num > 0:
        contadorPositivo += 1

print("Quantidade de pares: ", contadorPar)
print("Quantidade de positivos: ", contadorPositivo)
    
