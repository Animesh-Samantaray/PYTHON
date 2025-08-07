class account:
    def __init__(self,name,ac_no,balance):
        self.name=name
        self.ac_no=ac_no
        self.balance=int(balance)

    def deposit(self ,amount):
        print(f'{amount} rupees added to your account')
        self.balance +=amount
        print(f'Current balance : {self.balance}\n')

    def remove(self , amount):
        if amount>self.balance:
            print('balance is low\n')
            return
        
        print(f'{amount} rupees removed from your account')
        self.balance -=amount
        print(f'Current balance : {self.balance}\n')

    def details(self):
        print(f'Name -----> {self.name}')
        print(f'ac_no -----> {self.ac_no}')
        print(f'balance -----> {self.balance}\n\n')


s = account('Animesh Samantaray ','12345' , 1000)
s.details()
s.deposit(1233)

s.deposit(1233)
s.deposit(1233)
s.deposit(1233)

s.remove(100000)
s.remove(1000)
s.details()