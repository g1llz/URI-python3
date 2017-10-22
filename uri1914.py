qt = int(input())
cont = 0

while cont<qt:
	a, b, c, d = map(str, input().split())

	e, f = map(int, input().split())

	if b!=d:
		soma = e+f
		if soma%2==0:
			res = "PAR"
			if res == b:
				print(a)
			if res == d:
				print(c)

		else:
			res = "IMPAR"
			if res == b:
				print(a)
			if res == d:
				print(c)

	else:
		exit()

	cont+=1