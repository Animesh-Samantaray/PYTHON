# n=int(input('Enter number : '))
# s=str(n)
# b=[]
# for i in s:
#     if int(i)%2==0:
#         b.append(str(int(i)-1))
#     else:
#         b.append(str(int(i)+1))
# res=int(''.join(b))
# print(res)

    

def chk(m):
    r=len(m[0])
    for i in m:
        if len(i)!=r:
            return false