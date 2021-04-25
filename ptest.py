# Python test file
f=open("input.txt","r")
f.readline() #skip instruction line

for line in f:
  num=list(map(int,line.split(" ")))
  

f.close()
