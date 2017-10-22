
x = int(input())
cont = 0

while cont<x:
	y = int(input())
	aux = 0
	soma = 0

	while aux<y:
		if soma==0:
			soma = 1
		else:
			soma = 0
		aux+=1
			
	print(soma)
	cont+=1