class exam:
    def __init__(self, m , s , e):
        self.m=m
        self.s=s
        self.e=e
    
    def find(self):
        print(self.m , self.s , self.e)

st=exam(1,2,3)
st.find()
st.s=100
st.find()