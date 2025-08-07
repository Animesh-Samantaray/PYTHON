class math:
    def add(self,a,b,c=0,d=0): 
        return a+b+c+d
    # python doesnot support method overloading but in this way we can perform method overloading job
a = math()
print(a.add(1,2))
print(a.add(1,2,3))
print(a.add(1,2,3,4))