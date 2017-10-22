#temp = []
setlist = ['PROXYCITY', 'P.Y.N.G.', 'DNSUEY!', 'SERVERS', 'HOST!', 'CRIPTONIZE', 'OFFLINE DAY', 'SALT', 'ANSWER!', 'RAR?', 'WIFI ANTENNAS']
cont = 0

case = int(input())

while cont<case:
  a, b = map(int, input().split())
  soma = a+b
  if soma<len(setlist):
    #temp.append(soma)
    for index, music in enumerate(setlist):
      if index == soma:
        print(music)  
    
  cont+=1

#print(temp)

#for index, music in enumerate(setlist):
#      if index in temp:
#        print(music)  
    