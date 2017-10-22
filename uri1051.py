'''
URI 1051

'''

salario = float(input())


if (salario >= 0 and salario <= 2000):
  print("Isento")
  
elif (salario > 2000 and salario <= 3000):
  resultado = (salario - 2000) * 0.08
  print("R$ %0.2f" %resultado)
  
elif (salario > 3000 and salario < 4500):
  resto = salario - 3000
  resultado = ((salario - 3000) * 0.18) + (1000 * 0.08)
  print("R$ %0.2f" %resultado)
  
else:
  resultado = ((salario - 4500) * 0.28) + (1500 * 0.18) + (1000 * 0.08)
  print("R$ %0.2f" %resultado)