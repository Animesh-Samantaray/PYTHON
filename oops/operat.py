class student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self ,b):
        return self.marks+b.marks

s1=student(100)
s2=student(200)
print(s1+s2)