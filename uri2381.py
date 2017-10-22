a, b = map(int, input().split())
cont = 0
alunos = []
while cont<a:
  nome = input().lower()
  alunos.append(nome)
  
  cont+=1

alunos_formatado = sorted(alunos)

print(alunos_formatado[b-1])
  