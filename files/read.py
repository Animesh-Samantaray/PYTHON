# f=open('d:/PYTHON/files/demo.txt',"r")
# # data=f.read()
# line1 = f.readline()#it will read single line
# line2=f.readline()
# # all_lines = f.readlines()# it will read all lines
# # print(data) 
# print(line1)
# print(line2)
# # print(all_lines)

# data = f.read()
# print(data)
# f.close()


with open('pre.txt' , 'r') as f:
    print(f.read())
with open('pre.txt' , 'a') as f:
    f.write("123456789 \t")
