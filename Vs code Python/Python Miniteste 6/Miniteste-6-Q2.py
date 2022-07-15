M = [[1, 0, 2, 3 ],[4, 0, 5, 6], [0, 0, 0, 0], [0, 0, 0, 0]] 

def obtemLinhasNulas(matriz):
  linhasNulas = 0
  
  for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
      soma += matriz[i][j] 
    if soma == 0:
      linhasNulas += 1
 
  return linhasNulas

def obtemColunasNulas(matriz):
  colunasNulas = 0
  
  for i in range(len(matriz)):
    soma = 0
    for j in range(len(matriz[i])):
      soma += matriz[j][i] 
    if soma == 0:
      colunasNulas += 1
  
  return colunasNulas

print(f'Linhas: {obtemLinhasNulas(M)}')
print(f'Colunas: {obtemColunasNulas(M)}')

