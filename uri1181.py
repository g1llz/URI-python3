x = int(input())
op = input().upper()
matriz = []
soma = 0
for i in range(12):
  linha = []
  for i in range(12):
    n = float(input())
    linha.append(n)
  matriz.append(linha)
for i in matriz[x]:
  soma += i
if op == "S":
  print("%.1f"%soma)
elif op == "M":
  print("%.1f"%(soma/len(linha)))
