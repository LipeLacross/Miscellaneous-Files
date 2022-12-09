print("==Bem-vindo==")
print("==Esse programa detalha as características de um triângulo==")

ladosDoTriangulo = []

contador = 1
for i in range(3):
    num = int(input("Fale o valor do " + str(contador) + "º lado do triângulo: "))
    ladosDoTriangulo.append(num)
    contador = contador + 1

print("Sequência:", ladosDoTriangulo)

for i in ladosDoTriangulo:
    if i > 0:
        print(i,"É um Número válido.")
    else:
        print(i,"Não é um Número válido.")
        print("O lado de um triângulo não pode ser 0 ou menor que 0.")
        break
    
if (ladosDoTriangulo[0] + ladosDoTriangulo[1]) > ladosDoTriangulo[2]:
    if (ladosDoTriangulo[0] + ladosDoTriangulo[2]) > ladosDoTriangulo[1]:
        if (ladosDoTriangulo[1] + ladosDoTriangulo[2]) > ladosDoTriangulo[0]:
            print("Os lados correspondem à um triângulo.")
            if ladosDoTriangulo[0] == ladosDoTriangulo[1] == ladosDoTriangulo[2]:
                print("É um triângulo equilátero.")
            elif ladosDoTriangulo[0] == ladosDoTriangulo[1] or ladosDoTriangulo[1] == ladosDoTriangulo[2] or ladosDoTriangulo[0] == ladosDoTriangulo[2]:
                print("É um triângulo isósceles.")
            else:
                print("É um triângulo escaleno.")
        else:
            print("Os lados não correspondem à um triângulo.")
    else:
        print("Os lados não correspondem à um triângulo.")
else:
    print("Os lados não correspondem à um triângulo.")

print("Fim do programa.")