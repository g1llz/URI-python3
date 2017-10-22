'''
URI 1073

'''

x = int(input())

i = 1

while(i <= x):
	if(i%2 == 0):
	  calc = i ** 2
	  print("%d^2 = %d" %(i, calc))
	
	i = i + 1