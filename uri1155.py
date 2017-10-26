# S = 1 + 1/2 + 1/3 + … + 1/100

listNum = []

for n in range(2, 101):
  listNum.append(1/n)
  soma = sum(listNum)
  s = 1 + soma

print("%.2f" %s)
