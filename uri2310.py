saque = []
block = []
ataqu = []
saque1 = []
block1 = []
ataqu1 = []

c = int(input())
cnt = 0

while cnt<c:
  nome = input()
  s, b, a = map(int, input().split())
  saque.append(s)
  block.append(b)
  ataqu.append(a)
  s1, b1, a1 = map(int, input().split())
  saque1.append(s1)
  block1.append(b1)
  ataqu1.append(a1)
  
  cnt+=1
  
print("Pontos de Saque: {:.2f} %.".format((sum(saque1)/sum(saque))*100))
print("Pontos de Bloqueio: {:.2f} %.".format((sum(block1)/sum(block))*100))
print("Pontos de Ataque: {:.2f} %.".format((sum(ataqu1)/sum(ataqu))*100))