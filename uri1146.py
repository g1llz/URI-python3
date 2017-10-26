cont = 0

while (cont<1):
  x = int(input())
  
  if (x!=0):
    print(" ".join(str(n) for n in range(1, x+1)))
    
  else:
    cont+=1
    