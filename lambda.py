square = lambda x:x*2
add = lambda a,b:a+b
substract=lambda a,b:a-b
sqrt=lambda a:a**0.5
# print(square(2),add(1,2),substract(10,20),sqrt(109))

# lambda func is annynomus function without any name 

def call(fx , val):
    return val+fx(val)

print(call( lambda x:x**2,10)) #passing functin as arguments