class granpa:
    def __init__(self,name,origin):
        self.name=name
        self.origin=origin
    def show_det(self):
        print(f'Name : { self.name} \n origin:{self.origin}')
    
class father(granpa):
    def __init__(self, name, origin,height):
        super().__init__(name, origin)
        self.height=height
        
g = granpa('ANimesh' , 'oorr')
k = father('animesh' , 'foo' , 90);
k.show_det()

