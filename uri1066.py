'''
URI 1066

'''

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

lista = [n1, n2, n3, n4, n5]

i = 0
pares = 0
impares = 0
positivos = 0
negativos = 0

while (i < len(lista)):
  if (lista[i] %2 == 0):
    pares = pares + 1
    
  elif (lista[i] %2 != 0):
    impares = impares + 1
    
  if (lista[i] > 0):
    positivos = positivos + 1
  
  elif (lista[i] < 0):
    negativos = negativos + 1
    
  
  i = i + 1
  
  
print("%d valor(es) par(es)" %pares)
print("%d valor(es) impar(es)" %impares)
print("%d valor(es) positivo(s)" %positivos)
print("%d valor(es) negativo(s)" %negativos)