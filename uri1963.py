valorant, valornovo = map(float, input().split())

if (valorant>0) and (valornovo>=valorant):
  dif = ((valornovo-valorant)/valorant)*100
  print("{:.2f}%".format(dif))