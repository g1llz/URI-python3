cont = 0
nums = []

while cont<1:
  x = int(input())
  if x>=0:
    nums.append(x)
    
  else:
    cont+=1
  
soma = sum(nums)
media = soma / len(nums)

print("%0.2f" %media)    