numcoluna = int(input())
teste = str(input())
resultado = 0

matriz = []

for lin in range(12):
  linha = []
  while(len(linha)<12):
    temp = list(map(float,input().split()))
    for i in temp:
      linha.append(i)
  matriz.append(linha)

def coluna_matriz(matriz):
  colunas = []
  for i in range(len(matriz)):
    colunas.append(matriz[i][numcoluna])
    
  if "S" in teste:
    resultado = sum(colunas)
  elif "M" in teste:
    resultado = sum(colunas)/len(colunas)
  print("%0.1f" %resultado)

coluna_matriz(matriz) 