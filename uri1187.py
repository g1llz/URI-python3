matriz = []
soma = 0
m = 0
sub = 0
op = input().upper()
for i in range(12):
  linha = []
  for j in range(12):
    n = float(input())
    linha.append(n)
  matriz.append(linha)

for i in range(12):
  for j in range(12):
    if j > i and (j + i) < 11:
        soma += matriz[i][j]
        m += 1
if op == "S":
  print("%.1f"%soma)
elif op == "M":
  print("%.1f"%(soma/m))
