class Aanimesh(Exception):
    def __init__(self , msg='Animesh Error'):
        self.msg=msg
        super().__init__(msg)
        
raise Aanimesh()