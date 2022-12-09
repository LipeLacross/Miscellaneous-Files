# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual número ele deseja ver a tabuada. 
# A saída deve ser conforme o exemplo abaixo:

num = int(input("Qual o número da tabuado que você deseja gerar? "))

print("Tabudada de", num)
for valor in range(1,11):
    print(num,"X", valor,"=", num * valor)