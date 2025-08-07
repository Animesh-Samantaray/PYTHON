# f = open('demo.txt','a+');
# f.write('line 1\n\n')
# f.seek(0)# moves the reader at the 0th line
# data = f.read()
# print(data)
# f.close()

# a+  -> add at the end 
# r+ -> add at the starting

f = open('demo.txt', 'r+')
data = f.read()
for i in range(5):
    f.write('hii animesh \n')
   
f.seek(0,2)
f.write('\n')

f.close()
