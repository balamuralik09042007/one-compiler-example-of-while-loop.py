a=int(input())
count=0
temp=a
for i in range(1,a):
  if a%i==0:
    count=count+i
if temp==count:
  print("Perfect")
else:
  print("Not Perfect")
