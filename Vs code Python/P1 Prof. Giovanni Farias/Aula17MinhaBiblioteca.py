def fatorial(numero):
  print("DENTRO DA FUNÇÃO")
  if numero == 0:
    return 1
  i = numero
  fat = numero
  while i > 1:
    fat = fat * (i -1)
    i = i - 1
  return fat

def lerSequenciaInt(n):
  sequencia = []
  for i in range(n):
    numero = int(input("Digite um número: "))
    sequencia.append(numero)
  return sequencia

