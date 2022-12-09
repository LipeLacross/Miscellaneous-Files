'''
Comando continue
   - permite interromper a iteração corrente e continuar com a próxima iteração do laço
'''
numeros = [9, 8, 1, 10, 2, 4, 4, 9, 10, 5, 6, 4, 9, 4, 10, 6, 8, 2, 7, 3]

print("Números: ", numeros)

for num_atual in numeros:
    if (num_atual < 5):
        continue #Vai interromper a iteração corrente quando o if for verdadeiro e o laço continuará.
    print(num_atual)

print("Primeiro comando fora do for")