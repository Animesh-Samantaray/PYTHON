# class having abstract method is abstract class
# method without body is abstract method
# to use abstract class and metod import ABC(Abstract Base Classes) and abstract method
from abc import ABC,abstractmethod

class animal:
    # @abstractmethod
    def sound(self):
        pass
    
class tiger(animal):
    def sound(self):
        print('roaring')
class cat(animal):
    def sound(self):
        print('mewww...')

t=tiger()
t.sound()
c=cat()
c.sound()