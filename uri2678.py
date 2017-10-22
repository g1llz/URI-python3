rest = []
inic = []

cont = 0

while True:
    try:
        while cont == 0:
            telefone = input().upper()

            for i in telefone:
                if i == "A" or i == "B" or i == "C":
                    num = 2
                    rest.append(num)

                elif i == "D" or i == "E" or i == "F":
                    num = 3
                    rest.append(num)

                elif i == "G" or i == "H" or i == "I":
                    num = 4
                    rest.append(num)

                elif i == "J" or i == "K" or i == "L":
                    num = 5
                    rest.append(num)

                elif i == "M" or i == "N" or i == "O":
                    num = 6
                    rest.append(num)

                elif i == "P" or i == "Q" or i == "R" or i == "S":
                    num = 7
                    rest.append(num)

                elif i == "T" or i == "U" or i == "V":
                    num = 8
                    rest.append(num)

                elif i == "W" or i == "X" or i == "Y" or i == "Z":
                    num = 9
                    rest.append(num)

                else:
                    if i == "-" or i == "#" or i == "*":
                        pass

                    else:
                        inic.append(i)

            if telefone == "":
                cont += 1

            numero = inic + rest
            print("".join(map(str, numero)))
            inic = []
            rest = []

    except EOFError:
        break
