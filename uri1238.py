n = int(input())
for i in range(n):
  resposta = ""
  palavra1,palavra2 = map(str,input().split())
  palavramenor = ""  
  palavramaior = ""
  if len(palavra1)<=len(palavra2):
    palavramenor = palavra1
    palavramaior = palavra2
  else:
    palavramenor = palavra2
    palavramaior = palavra1
  
  for i in range(len(palavramenor)):
    resposta+=palavra1[i]+palavra2[i]
  resposta+=palavramaior[len(palavramenor):]
  print(resposta)
