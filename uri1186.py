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
aux = len(matriz)
for i in range(1,len(matriz)):
  aux-=1
  for col in range(aux,len(matriz[i])):
    listatemp.append(float(matriz[i][col]))
if "S" in teste:
  resultado = sum(listatemp)
elif "M" in teste:
  resultado = sum(listatemp)/len(listatemp)
print("%0.1f" %resultado)
