def fatorial(x):
    if x == 0 or x == 1:
      return 1 
    return x * fatorial(x - 1)
try:
  while True:
    v1,v2 = map(int,input().split())
    print(fatorial(v1)+fatorial(v2))
except:
  pass
