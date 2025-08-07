l = ['Animesh' , 'Rakesh' , 'Suresh' ,'Raj' ,12,23,34,45,56,67,]

def find(x):
    k=0
    for i in x:
        k+=1
    return k

def print_in_single_line(l):

    for i in range(len(l)):
        print(l[i],end=" ") # use for cutting \n

length = find(l)
print(length)
print_in_single_line(l)
