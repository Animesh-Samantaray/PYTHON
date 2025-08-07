data={
    "name":"Animesh",
    "age":18,
    'height':12233,
    "student":{
        'id':1,
        'w':122
    }
}

# x=list(data.keys());#  keys will return all the remaining keys present in the dictionary
# print(x);
# l  = list(data.items()) #items will return thr key value pair in form of () tuple
# l1=list(l[0])
# l1.append('animesh')
# print(l1)
# print(l)

print(data.get('student'))
