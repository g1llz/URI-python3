x = 0
y = 1

soma = "0 "

num = int(input())
cont = 1

while cont<num:
	soma = soma + str(y)+" "
	x, y = y, x+y
	cont+=1

print(soma[0:-1])