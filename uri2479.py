num = int(input())
cont = 0
bom = 0
mal = 0
ttl = []

while cont<num:
  a, b = map(str, input().split())
  
  if a == "+":
    ttl.append(b)
    bom+=1
  if a == "-":
    ttl.append(b)
    mal+=1
    
  cont+=1
  
ttl.sort()

print("\n".join(map(str, ttl)))
print("Se comportaram: {} | Nao se comportaram: {}".format(bom, mal))
    
  
