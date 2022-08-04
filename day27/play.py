
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add())



def calculate(n,**kwargs):
    
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)

calculate(2,add = 3,mul = 5,)

class Car:
    def __init__(self,**kw) -> None:
        self.make = kw["make"]
        self.model = kw["model"]
        

        pass

car = Car(make ="lambor",model = "ezpz")
print(car.model)