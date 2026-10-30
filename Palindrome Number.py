a=int(input())
temp=a
count=0
while a>0:
  total=a%10
  count=(count*10)+total
  a=a//10
if temp == count:
  print("Palindrome")
else:
  print("Not Palindrome")
