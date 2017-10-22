'''
URI 1048

'''

sal_base = input()
sal_base = float(sal_base)

if (sal_base >= 0.00 and sal_base <= 400.00):
  reajuste = sal_base * 0.15
  saldo = sal_base + reajuste
  print("Novo salario: %0.2f" %saldo)
  print("Reajuste ganho: %0.2f" %reajuste)
  print("Em percentual: 15 %")

if (sal_base > 400.00 and sal_base <= 800.00):
  reajuste = sal_base * 0.12
  saldo = sal_base + reajuste
  print("Novo salario: %0.2f" %saldo)
  print("Reajuste ganho: %0.2f" %reajuste)
  print("Em percentual: 12 %")

if (sal_base > 800.00 and sal_base <= 1200.00):
  reajuste = sal_base * 0.1
  saldo = sal_base + reajuste
  print("Novo salario: %0.2f" %saldo)
  print("Reajuste ganho: %0.2f" %reajuste)
  print("Em percentual: 10 %")
  
if (sal_base > 1200 and sal_base <= 2000.00):
  reajuste = sal_base * 0.07
  saldo = sal_base + reajuste
  print("Novo salario: %0.2f" %saldo)
  print("Reajuste ganho: %0.2f" %reajuste)
  print("Em percentual: 7 %")

if (sal_base > 2000.00):
  reajuste = sal_base * 0.04
  saldo = sal_base + reajuste
  print("Novo salario: %0.2f" %saldo)
  print("Reajuste ganho: %0.2f" %reajuste)
  print("Em percentual: 4 %")