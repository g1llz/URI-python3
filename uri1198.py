
while True:
	try:

		x, y = map(int, input().split())

		if x>=y:
			dif = x-y
			print(dif)
		else:
			dif = y-x
			print(dif)
	
	except:
		break



