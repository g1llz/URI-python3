'''
URI 1070

'''

x = int(input())

a = int
b = int
c = int
d = int
e = int
f = int

if(x %2 == 0):
  a=x+1
  b=x+3
  c=x+5
  d=x+7
  e=x+9
  f=x+11

elif(x %2 != 0):
  a=x
  b=x+2
  c=x+4
  d=x+6
  e=x+8
  f=x+10

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)