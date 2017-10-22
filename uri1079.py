'''
URI 1079

'''

x = int(input())
cont = 0
valores = []

while cont<x:
	a, b, c = input().split(" ")
	a = float(a)
	b = float(b)
	c = float(c)
	
	valores.append([a, b, c])

	cont += 1

for n in valores:
	soma = ((n[0] * 2) + (n[1] * 3) + (n[2] * 5)) / 10
	print("%0.1f" %soma)