n=int(input('enter :'))
a=0
b=1
sum=0
l=[]
for i in range(n):
    l.append(sum)
    sum=a+b
    a=b
    b=sum
print(l)