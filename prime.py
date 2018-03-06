a=input('enter the number')
i=2
a=int(a)
while i<a:
  flag=0
  j=2
  while j<i:
     if i%j==0:
        flag=flag+1
     j=j+1
  if flag==0:
    print(i)
  i=i+1


