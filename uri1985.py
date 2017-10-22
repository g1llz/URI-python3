vnda = [['1001', '1.5'], ['1002', '2.5'], ['1003', '3.5'], ['1004', '4.5'], ['1005', '5.5']]
soma = 0

p = int(input())
if p>=1 and p<=5:
  for n in range(0, p):
    prod, qtd = input().split()
    qtd = int(qtd)
    
    for i in vnda:
      if i[0]==prod:
        soma = soma + (float(i[1])*qtd)
      
print("{:.2f}".format(soma))
    