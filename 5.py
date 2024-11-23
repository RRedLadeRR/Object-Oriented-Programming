class Car:
    total = 0

    @staticmethod
    
    def status():
        print("Total number of cars", Car.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Car.total += 1
    
def main():
    print("Attribute acess Car.total class:", end=(" "))
    print(Car.total)

    print("Cars starting")
    car1 = Car("Car №1")
    car2 = Car("Car №3")
    car3 = Car("Car №3")

    Car.status()

    print("Class attribute acess with object:", end=" ")
    print(car1.total)

main()