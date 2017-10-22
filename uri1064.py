'''
URI 1064

'''

# declara que haverá 6 entradas com numeros 'float' (ex. 3.2, -4.1, 2.0)

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

# agrupa as entradas 'n' em uma 'lista'. nesse exemplo, a 'lista' se chama lista.

lista = [n1, n2, n3, n4, n5, n6]

i = 0

# cria outra lista vazia, chamada 'positivos'.

positivos = []

# while é um comando de repetição. e seu disparador é: quando 'i' for menor que o comprimento da lista, rode.
# len(lista) é o 'comprimeto' (quantidade de numeros/nomes/informações na lista).

while (i < len(lista)):
  if (lista[i] > 0):
    positivos.append(lista[i]) # todo valor maior que 'zero', será adicionado a lista 'positivos'.
  i = i + 1
  
i = 0
resultado = 0

while (i < len(positivos)): #roda a lista 'positivos' usando o mesmo disparador 'i menor que comp. da lista'
  resultado = resultado + positivos[i]
  i = i + 1

# faz o cálculo da média pegando a soma dos numeros positivos e dividindo pela quantidade dos mesmos.

media = resultado / len(positivos)
qtde = len(positivos)

# saida do programa que imprime: 'X (quantidade de numeros) valores positivos'.
#                                'X (valor da média)'

print("%d valores positivos" %qtde)
print("%0.1f" %media)