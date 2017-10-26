# Ler um número inteiro N e calcular todos os seus divisores.

x = int(input())

for n in range(1, x+1):
  if x%n == 0:
    print(n)