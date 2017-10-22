
while True:
  try:
    jogadores = int(input())
    
    votos = input()
    votos_formatados = votos.split()
    
    favoravel = 0
    contra = 0
      
    for i in votos_formatados:
      if int(i) == 1:
        favoravel+=1
      else:
        contra+=1
          
    #print(favoravel)
    #print(contra)
    
    divisao = (jogadores/3)*2
    
    #print (divisao)
    
    if favoravel >= divisao:
      print("impeachment")
    else:
      print("acusacao arquivada")
        
  except:
    break
  