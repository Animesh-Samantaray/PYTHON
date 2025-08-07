# class student:

#     def __init__(self):
#         self.name="Student without name"
#         self.age="student without age"
#         print('Not entered any data')

#     def set(self,name,age):
#         self.name=name
#         self.age=age
#         print(f'name:{self.name}      age:{self.age}');

# s= student()
# s.set('Animesh ' , 100)

class user:
    def __init__(self , name ):
        self.name=name

    def getPass(self):
        return self.__password #            use __name for privating
    
    def setPass(self,val):
        self.__password = val

user1 = user('Animesh' )
print(user1.name)
user1.setPass('11223344')
print(user1.getPass())
# print(user1.__password)

