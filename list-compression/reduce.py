from functools import reduce

arr = [1,2,3,4,5]

# def sum(a,b):
#     return a+b

k=reduce(lambda x,y: x*y,arr)
print(k)