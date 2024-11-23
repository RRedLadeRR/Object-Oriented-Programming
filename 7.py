class Car:
    
    total = 0

    @staticmethod
    
    def status():
        print("Total number of cars", Car.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.__name = name
        self.hunger = hunger
        self.boredom = boredom
        Car.total += 1

    def talk(self):
        print("Wroom Wroom", self.__name)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Car name cannot be empty")
        else:
            self.__name = new_name
            print("Name successfully changed")
    
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