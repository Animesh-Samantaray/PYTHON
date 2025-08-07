# # set is mutable
# # data in set is unmutable

# s=set()
# s.add(1)
# s.add(2)
# print(s)
# s.remove(2)
# print(s)
# s.clear()#remove all values
# print(s)

# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# print(s)

# s.pop()#remove random value
# print(s)

#                                       union
s={2,3,4,5,6,7}
t={2,3,'y',True}
s1=s.union(t)
print(s1)
#                                       intersection
s2=s.intersection(t)
print(s2)