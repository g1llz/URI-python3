'''
URI 1072

'''

l = []
somax = 0
somay = 0

a = int(input())

for n in range(1,(a+1)):
    l.append(input())

for n in l:
    if (10<=int(n)<=20):
        somax += 1
    elif (int(n)>20) or (int(n)<10):
        somay += 1

print(somax,"in")
print(somay,"out")