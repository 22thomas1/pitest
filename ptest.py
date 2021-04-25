# Python test file
f=open("input.txt","r")

for line in f:
  num=map(int,line.split(" "))
  for x in num:
      print(x)

f.close()
