class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def show_complex(self):
        print(f'\n num = {self.real}i + {self.img}j')

    # @staticmethod
    # def add(a,b):
    #     i = a.real+b.real
    #     j=a.img+b.img
    #     return complex(i,j)
    
    def __add__(a,b):# operator overloading on +
        i = a.real+b.real
        j=a.img+b.img
        return complex(i,j)
    
    def __sub__(a,b):# operator overloading on -
        i = a.real-b.real
        j=a.img-b.img
        return complex(i,j)

c1=complex(1,1)
c2=complex(2,2)
c3=complex(3,3)
c4=c1+c2+c3
c4.show_complex()