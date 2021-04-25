# Python test file
f=open("input.txt","r")

while true:
  num=map(int,f.readline().split(" "))
  if num=="":
    break
  for x in num:
      print(x)

f.close()
