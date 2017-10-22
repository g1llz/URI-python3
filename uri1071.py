'''
URI 1071

'''
a = int(input())
b = int(input())
soma = 0
for n in range((b+1), a):
    if (n%2!=0):
        soma += n #> mesma coisa que soma = soma + n
print(soma)