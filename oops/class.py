class student:
    def __init__(self,name,age,title):
        self.name=name
        self.age=age
        self.title=title

    @staticmethod
    def show():
        print('I am a static method.....boom')
        return 100

    def show_details(self):
        print(self.name,self.age,self.title)

s=student('ani' , '12','rr')
        
student.show()# used class to call the static method