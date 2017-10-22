

while True:

	try:

		x = int(input())

		cont = 1
		aux = 2

		if x>1:
			while aux<x:
				z = aux
				cont+=1
				z = aux+z
				aux*=2 
			print(cont)


		if x==1:
			print("0")

	except:
		break


