cont = 0
nums = []
soma = 0

while cont<1:
  x = int(input())
  if x==0:
    cont+=1
  
  else:
    nums.append(x)
    
for n in nums:
  if n/2==0:
    for i in range(n, n+9):
      if i%2==0:
        soma += i
    print(soma)
    soma = 0
    
  if n/2!=0:
    for i in range(n, n+10):
      if i%2==0:
        soma += i
    print(soma)
    soma = 0
    