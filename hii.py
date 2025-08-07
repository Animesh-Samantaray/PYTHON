#ask the user to enter her mobile number
#make a list of unique present in the numebrs
#make another list 'b' which consist of the digits not present in the number
#create a square matrix of all prime numbers less than min number that can be formed using the digits present in b(append 0 if required)
# find all the diagonal elements of the square matrix
#replace all the values greater than the avg value with 1 and others with 0
# import numpy as np
mobile = input('Enter mobile number : ')

l=list(set(mobile))
print(l)

num = {'0','1','2','3','4','5','6','7','8','9'}
b=list(num-set(mobile))
print(b)

min = int(''.join(sorted(b)))
print(min)

def isPrime(n):
    if n<2: 
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

pr = []
for i in range(2,min):
    if isPrime(i):
        pr.append(i)

print(pr)