listNum = []
rep = int(input())
cont = 0
aux = 0
resto = []
soma = 0

while (cont<rep):
  x, y = map(int, input().split())
  listNum.append([x, y])
  
  cont+=1


while rep<len(listNum):
	for i in range(x+1, y):
		if i%2!=0:
			soma += i
			resto.append(soma)

	

	aux+=1
print(resto)  