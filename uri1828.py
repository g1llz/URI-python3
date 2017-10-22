'''
1 - a tesoura corta o papel;
2 - o papel embrulha a pedra;
3 - a pedra esmaga o lagarto;
4 - o lagarto envenena Spock;
5 - Spock destrói a tesoura;
6 - a tesoura decapita o lagarto;
7 - o lagarto come o papel;
8 - o papel contesta Spock;
9 - Spock vaporiza a pedra;
0 - a pedra quebra a tesoura.
'''

x = int(input())
cont = 1

tesoura = ['papel','lagarto']
papel = ['pedra', 'Spock']
pedra = ['lagarto', 'tesoura']
lagarto = ['Spock', 'papel']
Spock = ['pedra', 'tesoura'] 

while cont<=x:
	a, b = map(str, input().split())

	if a==b:
		print("Caso #{}: De novo!".format(cont))

	else:
		if a=="tesoura":
			aux = 0
			for i in tesoura:
				if i==b:
					aux+=1
					
			if aux!=0:
				print("Caso #{}: Bazinga!".format(cont))
				
			else:
				print("Caso #{}: Raj trapaceou!".format(cont))
				
				

		elif a=="papel":
			aux = 0
			for i in papel:
				if i==b:
					aux+=1
					
			if aux!=0:
				print("Caso #{}: Bazinga!".format(cont))
				
			else:
				print("Caso #{}: Raj trapaceou!".format(cont))
				

		elif a=="pedra":
			aux = 0
			for i in pedra:
				if i==b:
					aux+=1
					
			if aux!=0:
				print("Caso #{}: Bazinga!".format(cont))
				
			else:
				print("Caso #{}: Raj trapaceou!".format(cont))
				

		elif a=="lagarto":
			aux = 0
			for i in lagarto:
				if i==b:
					aux+=1
					
			if aux!=0:
				print("Caso #{}: Bazinga!".format(cont))
				
			else:
				print("Caso #{}: Raj trapaceou!".format(cont))
				

		elif a=="Spock":
			aux = 0
			for i in Spock:
				if i==b:
					aux+=1
					
			if aux!=0:
				print("Caso #{}: Bazinga!".format(cont))
				
			else:
				print("Caso #{}: Raj trapaceou!".format(cont))
				
	cont+=1

