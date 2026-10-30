a=int(input())
count=1
while a>0:
  total=a%10
  count=count*total
  a=a//10
print(count)
