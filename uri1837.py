
import math

'''
a, b = map(int, input().split())

if a<0:
	if b<0:
		quociente = (a / b) + 1
		resto = a - int(quociente) * b
	else:
		quociente = (a / b) - 1
		resto = a - int(quociente) * b

if a>0:
	if b<0:
		quociente = a / b
		resto = a - int(quociente) * b
	else:	
		quociente = a / b
		resto = a - int(quociente) * b 	

print("{} {}".format(int(quociente), resto))
'''


a, b = map(int, input().split())

if math.fabs(a) == math.fabs(b):
    q = (a/b)
    q = math.floor(q)            
elif a<0 and b>0:
    q = (a/b)-1
    q = math.floor(q)       
elif a<0 and b<0:
    q = (a/b)+1
    q = math.floor(q)   
else:
    q = (a/b)
    q = math.floor(q)

r = a - (q * b)

print(q, r)

'''
a, b = map(int, input().split())

q = a/b
r = a%b

if r<0:
	if int(q)>0:
		q = q+1

	if int(q)<0:
		q = q-1

	r = a - (int(q)*b)

print("{} {}".format(int(q), r))
'''