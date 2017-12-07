while True:
  x = int(input())
  if x != 0:
    y = input().split()
    listaoficial = []    
    for i in range(x):
      a = int(y[i])
      listaoficial.append(a)
    zero = listaoficial.count(0)
    um = listaoficial.count(1)
    print("Mary won %d times and John won %d times"%(zero,um))
  else:
    break
