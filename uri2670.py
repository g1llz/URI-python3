a1 = int(input())
a2 = int(input())
a3 = int(input())

if a1>a2 and a1>a3:
	calc = (a2*2)+(a3*4)
	print(calc)

elif a2>a1 and a2>a3:
	calc = (a1*2)+(a3*2)
	print(calc)

elif a3>a1 and a3>a2:
	calc = (a1*4)+(a2*2)
	print(calc)

elif a1==a2 and a1==a3:
	calc = (a1*2)+(a3*2)
	print(calc)

elif a1==a2 and a2!=a3:
	calc = (a1*2)+(a3*2)
	print(calc)

elif a1!=a2 and a2==a3:
	calc = (a1*2)+(a3*2)
	print(calc)
