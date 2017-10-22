#import math

casosTeste = 0
a = 0
b = 0 
taxaa = 0
taxab = 0

casosTeste = int(input())

while(casosTeste > 0):
    a, b, taxaa, taxab = input().split()
    a, b, taxaa, taxab = float(a), float(b), float(taxaa), float(taxab)
    
    continua = True
    anos = 0

    while(continua):
        a += (taxaa * a) // 100
        b += (taxab * b) // 100
        #a = math.floor(a)
        #b = math.floor(b)

        if(a > b):
            continua = False
        if(anos > 100):
            continua = False
        anos += 1
        
    casosTeste -= 1
    if(anos > 100):
        print("Mais de 1 seculo.")
    else:
        print (str(anos)+ " anos.")