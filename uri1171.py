import collections

lista = []
qtd_vezes = int(input())
for i in range(qtd_vezes):
  lista.append(int(input()))
freq = collections.Counter(lista).most_common()
freq.sort()
for l in range(len(freq)):
  print("%s aparece %s vez(es)"%(freq[l][0],freq[l][1]))
