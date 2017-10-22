
casos = int(input())
temp = []
aux = 1
perfeito = []
imperfeito = []

while aux<=casos:
	num = int(input())

	for n in range(1, num):
		if num%n==0:
			temp.append(n)

	calc = sum(temp)

	if calc == num:
		perfeito.append(str("%d eh perfeito" %num))
		temp = []
	else:
		imperfeito.append(str("%d nao eh perfeito" %num))
		temp = []

	aux+=1

print(perfeito)
print(imperfeito)