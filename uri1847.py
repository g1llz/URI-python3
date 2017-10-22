while True:
  try:
    d1, d2, d3 = input().split()
    
    if d1<d2 and d2<d3:
      print(":)")
    
    if d1>d2 and d2>d3:
      print(":(")
      
    if d1>d2 and d3>=d2:
      print(":)")
    
  
  except Exception:
    break