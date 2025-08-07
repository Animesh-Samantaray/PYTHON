arr=[1,2,3,4,5,6,7,8,9,]
print(arr)
brr=list(filter(lambda x :x>4 , arr))
print(brr)
x=list(filter(lambda x : x%2==0 , arr))
print(list(filter(lambda x : x%3==0 , arr)))
