lista_yes = []
lista_no = []

aux = 0
nome_maior = ""

while True:
  nome = input().split()
  if nome[0] == "FIM":
    break
  if nome[1] == "YES" and nome[0] not in lista_yes:
    lista_yes.append(nome[0])
  if nome[1] == "NO":
    lista_no.append(nome[0])

for i in sorted(lista_yes):
  print(i)

for i in sorted(lista_no):
  print(i)

for i in lista_yes:
  if len(i) > aux:
    nome_maior = i
    aux = len(i)
    
print("\nAmigo do Habay:")
print(nome_maior)