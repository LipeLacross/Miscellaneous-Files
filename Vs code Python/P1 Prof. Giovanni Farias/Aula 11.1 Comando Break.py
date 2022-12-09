'''
Comando break
   - permite interromper a execução do laço antes que todos os elementos 
   da sequencia tenham sido atribuídos à variável de controle
'''
numeros = [9, 8, 1, 10, 2, 4, 4, 9, 10, 5, 6, 4, 9, 4, 10, 6, 8, 2, 7, 3]

print("Números: ", numeros)

for num_atual in numeros:
    if (num_atual < 5):
        break #Vai interromper completamente o laço for quando o if for verdadeiro
    print(num_atual)

print("Primeiro comando fora do for")