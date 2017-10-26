cont = 0
l = []
aux = 0

while cont<20:
  x = int(input())
  l.append(x)
  
  cont+=1

for n in l[::-1]:
  print("N[%d] = %d" %(aux, n))
  aux+=1
