x = int(input())
y = int(input())
soma = 0
if (x<y):
  for n in range(x, y+1):
    if (n % 13 != 0):
      soma += n
if (x>y):
  for n in range(y, x+1):
    if (n % 13 != 0):
      soma += n
  
print(soma)
  