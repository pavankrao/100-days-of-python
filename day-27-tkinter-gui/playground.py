
# *args example
def sum_of_nums(*args): # args is a tuple
    print(args[0])
    return sum(args)

print(sum_of_nums(1,2,3,4))


# **kwargs example
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make", "undefined")
        self.model = kw.get("model", "undefined")
        self.color = kw.get("color", "undefined")
        self.seats = kw.get("seats", 4)

car1 = Car(make="Honda", seats=6)

print(car1.make)
print(car1.color)
