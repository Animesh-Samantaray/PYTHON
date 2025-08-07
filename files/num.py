with open('num.txt','r') as f:
    data=f.read()

s=""
l=[]
# for i in range(len(data)):
#     if data[i] == ',':
#         l.append(int(s))
#         s=""
#     else:
#         s+=data[i]

l=data.split(',')
for i in range(len(l)):
    l[i]=round(int(l[i])/2)
print(l)