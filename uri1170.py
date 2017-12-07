x = int(input())
cont = 0
for i in range(x):
  n = float(input())
  while n >1:
    n /= 2
    cont += 1
  print(cont,"dias")
  cont = 0
