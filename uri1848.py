# URI 1848

temp = []

while True:
	try:
		x = input()

		if x == "---":
			num = 0
			temp.append(num)

		elif x == "--*":
			num = 1
			temp.append(num)

		elif x == "-*-":
			num = 2
			temp.append(num)

		elif x == "-**":
			num = 3
			temp.append(num)

		elif x == "*--":
			num = 4
			temp.append(num)

		elif x == "*-*":
			num = 5
			temp.append(num)

		elif x == "**-":
			num = 6
			temp.append(num)

		elif x == "***":
			num = 7
			temp.append(num)

		elif x == "caw caw":
			print(sum(temp))
			temp = []

	except Exception:
		break
