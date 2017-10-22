while True:
  try:
    
    h, m = map(int, input().split(":"))
    
    if h < 7:
      print("Atraso maximo: 0")
    elif h == 7:
      if m == 0:
        print("Atraso maximo: 0")
      else:
        print("Atraso maximo:",m)
    else:
      if m == 0:
        print("Atraso maximo: {}".format((h-7)*60))
      else:
        print("Atraso maximo: {}".format((h-7)*60+m))
  
  except:
    break