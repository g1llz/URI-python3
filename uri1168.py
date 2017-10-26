n = int(input())
cont = 0
soma = 0
listaStr = []

while cont < n:
  x = str(input())
  for i in x:
    if i == "1":
      soma+=2
    if i == "2":
      soma+=5
    if i == "3":
      soma+=5 
    if i == "4":
      soma+=4
    if i == "5":
      soma+=5
    if i == "6":
      soma+=6
    if i == "7":
      soma+=3
    if i == "8":
      soma+=7
    if i == "9":
      soma+=6
    if i == "0":
      soma+=6
  
  listaStr.append(soma)  
  soma = 0
  cont+=1

for i in listaStr:
  print(i, "leds")