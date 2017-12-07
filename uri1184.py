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

listatemp = []

def acima_da_diagonal(matriz):
  for lin in range(1,len(matriz)):
    for col in range(lin):
      listatemp.append(float(matriz[lin][col]))
  
  if "S" in teste:
    resultado = sum(listatemp)
  elif "M" in teste:
    resultado = sum(listatemp)/len(listatemp)
  return resultado
print("%0.1f" %acima_da_diagonal(matriz))