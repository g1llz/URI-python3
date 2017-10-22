c = int(input())
rpm = input().split()
qda = []

aux = 0

for index, i in enumerate(rpm):
  if int(i)>=int(aux):
    aux = i
  else:
    qda.append(index+1)

if qda == []:
  print("0")
else:
  print(qda[0])