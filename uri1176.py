qtd = int(input())
for i in range(qtd):
    fib = [0,1]
    n = int(input())
    if (n>1):
        for i in range(2,n+1):
            fib.append(fib[i-1]+fib[i-2])
    
        print("Fib(%d) = %d" %(n,fib[n]))
    else:
        print("Fib(%d) = %d" %(n,fib[n]))