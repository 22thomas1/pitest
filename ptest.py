# Python test file
f=open("input.txt","r")
for x in range(4):
  num=f.readline().split(" ")
  num=map(int,num)
  for x in num:
    print(x)
  print("\n")


  
  
f.close()
