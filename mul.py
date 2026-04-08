i=1
for i in range(1,100):
  if i%4!=0 & i%6!=0:
      i+=i
      print(i)
      continue
      if i%4==0 & i%6==0:
       print(i)
