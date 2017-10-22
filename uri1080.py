'''
URI 1080

'''

cont = 0
lista = []

while cont<100:
  x = int(input())
  lista.append(x)
  
  cont += 1

nMax = max(lista)
posicao = lista.index(nMax)
  
print(nMax)
print(posicao+1)