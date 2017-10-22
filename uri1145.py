# URI 1145 (estudar mais!)

x, y = map(int, input().split())
aux = 0
z = x

lista = []

for n in range(1, y+1):
	lista.append(n)
	aux+=1
	if aux==z:
		lista.append("x")
		z = aux+x

for elemento in lista:
	if elemento!="x":
		print(elemento,end=" ")
	else:
		print("")