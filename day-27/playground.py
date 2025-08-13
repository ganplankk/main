
def add(*args):
    print(args)
    print(args[1])
    sum = 0
    for i in args:
        sum += i

    return sum

print(add(1,2,3,4,5))


def calc(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    print(kwargs["add"])
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calc(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get("color")

my_car = Car(make = "benz", model = "Sclass")
print(my_car.make)
print(my_car.model)
print(my_car.color)