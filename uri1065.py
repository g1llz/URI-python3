'''
URI 1065

'''

# declara que haverá 5 entradas com numeros 'float' (ex. 3.2, -4.1, 2.0)

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

# agrupa as entradas 'n' em uma 'lista'. nesse exemplo, a 'lista' se chama lista.

lista = [n1, n2, n3, n4, n5]

i = 0
pares = 0

# while é um comando de repetição. e seu disparador é: quando 'i' for menor que o comprimento da lista, rode.
# len(lista) é o 'comprimeto' (quantidade de numeros/nomes/informações na lista).

while (i < len(lista)):
  if (lista[i] %2 == 0):
    pares = pares + 1
    
  i = i + 1

# saida do programa que imprime: 'X (quantidade de numeros) valores pares'.

print("%d valores pares" %pares)