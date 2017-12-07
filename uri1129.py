while True:
  entrada = int(input())
  if entrada!=0:
      
    for i in range(entrada):
      valores = input().split()
      contador = 0
      posicao = 0
      for i in valores:
        
        if int(i) <=127:
          contador+=1
          posicao = valores.index(i)
      if contador!=1:
        print("*")
      else:
        if posicao==0:
          print("A")
        elif posicao==1:
          print("B")
        elif posicao==2:
          print("C")
        elif posicao==3:
          print("D")
        elif posicao==4:
          print("E")
  else:
    break
