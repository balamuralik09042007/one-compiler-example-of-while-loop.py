a=int(input())
count=0
temp=a
digith=len(str(a))
while a>0:
  total=a%10
  count=(total**digith)+count
  a=a//10
if temp==count:
  print("Armstrong")
else:
  print("Not Armstrong")
