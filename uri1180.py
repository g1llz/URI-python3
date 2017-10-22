# Falta configurar as entradas

lista = list(map(int, input().split()))

d = min(lista)
print("Menor valor: %d" %d)
for i in lista:
	if i == d:
		print("Posica: %s" %lista.index(i))
