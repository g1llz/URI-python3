dnv = 1
gas = 0
alc = 0
dis = 0

while (dnv == 1):
  x = int(input())
  if (x == 1):
    alc += 1
  elif (x == 2):
    gas += 1
  elif (x == 3):
    dis += 1
  elif (x == 4):
    dnv += 1
    print("MUITO OBRIGADO")
    print("Alcool: %d" %alc)
    print("Gasolina: %d" %gas)
    print("Diesel: %d" %dis)
    
  else:
    dnv = 1
    
  
