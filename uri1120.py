def retira_tecla(x,y):
  resultado = ""
  for i in valor2:
    if i!=valor1:
      resultado+=i
  if len(resultado)==0:
    resultado="0"
  print(int(resultado))

while True:
  valor1,valor2 = map(str,input().split())
  if valor1!="0" and valor2!="0":
    retira_tecla(valor1,valor2)
  else:
    break
