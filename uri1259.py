x = int(input())
cont = 0
par = []
impar = []


while cont<x:
  num = int(input())
  if num%2==0:
    par.append(num)
  else:
    impar.append(num)
    
  cont+=1
  
par = sorted(par)
impar = sorted(impar)
impar = impar[::-1]

for i in par:
  print(i)

for i in impar:
  print(i)
  