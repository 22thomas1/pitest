# Python test file
f=open("input.txt","r")

for line in f:
  num=list(map(int,line.split(" ")))
  print(num[1])

f.close()
