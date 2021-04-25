# Python test file
f=open("input.txt","r")

for line in f:
  print(line)
  num=map(int,f.readline().split(" "))
  for x in num:
      print(x)

f.close()
