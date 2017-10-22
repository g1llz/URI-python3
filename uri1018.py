'''
URI 1018

'''

n = int(input())

if (0 < n < 1000000):
  
  cem = n/100
  cin = n%100/50
  vin = n%50/20
  dez = n%100%50%20/10
  cinco = n%10/5
  dois = n%5/2
  um = n%100%50%20%10%5%2/1

  print("%d" %n)
  print("%d nota(s) de R$ 100,00" %cem)
  print("%d nota(s) de R$ 50,00" %cin)
  print("%d nota(s) de R$ 20,00" %vin)
  print("%d nota(s) de R$ 10,00" %dez)
  print("%d nota(s) de R$ 5,00" %cinco)
  print("%d nota(s) de R$ 2,00" %dois)
  print("%d nota(s) de R$ 1,00" %um)