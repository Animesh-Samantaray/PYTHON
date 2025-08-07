def call(l , i):
    if i>=len(l):
        return
    print(l[i],end="  ")
    call(l,i+1)

l=[1,2,3,3,2,1,4,98]
call(l,0)
