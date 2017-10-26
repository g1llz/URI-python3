x = int(input())
y = int(input())

if (x<y):
  for n in range(x+1, y):
    if ((n % 5 == 2) or (n % 5 == 3)):
      print(n)
      
if (x>y):
  for n in range(y+1, x):
    if ((n % 5 == 2) or (n % 5 == 3)):
      print(n)
  