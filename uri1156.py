s = 1
n1 = 3
n2 = 2
cont = 0
while n1 < 40:
    s = s + (n1/n2)
    n1 += 2
    n2 = n2 * 2
print("%.2f" %s)