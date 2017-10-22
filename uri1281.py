frutas = []
precos = []
soma = 0

feira = int(input())
for i in range(feira):
  qtd_prod = int(input())
  for i in range(qtd_prod):
    f, p = input().split()
    p = float(p)
    frutas.append(f)
    precos.append(p)
  
  qtd_comp = int(input())
  for i in range(qtd_comp):
    f1, qtd = input().split()
    qtd = int(qtd)
    for i, j in zip(frutas, precos):
      if f1 == i:
        soma = soma + qtd * j
  
  
  print("R$ {:.2f}".format(soma))
  frutas = []
  precos = []
  soma = 0