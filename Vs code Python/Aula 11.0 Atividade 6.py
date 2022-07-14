#  A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input("Digite o tamanho desejado da sequência: "))

fib = [1, 1]
for i in range(2,n):
    fib.append(fib[i-2] + fib[i-1])

print(fib)