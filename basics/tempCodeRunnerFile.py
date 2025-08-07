l=[1 , 2 , 3.0 , True,3.0 , 3.1]#list mutable 
l.append(122)
print(l)

l.sort(reverse=True) #sorts on decreasing value
l.reverse()# reverses
# print(l)
l.insert(1 , 122)
# print(l)
l.remove(3) # it will remove 1st occurence of the data traversing from the first
# print(l);
l.pop(4)
print(l)