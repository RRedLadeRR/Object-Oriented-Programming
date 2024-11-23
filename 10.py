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
        print("Wroom Wroom", self.__name, "Status: ", self.mood)
        self.__pass_time()

    def eat(self, food = 4):
        print("Wroom Wroom")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    @property
    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "wonderful"
        elif 5 <= unhappines <= 10:
            m = "not bad"
        elif 11 <= unhappines <= 15:
            m = "bad"
        else:
            m = "terrible"
        return m
    
def __pass_time(self):
    self.hunger += 1
    self.boredom += 1

def play(self, fun = 4):
    print("Wroooom Wroooom")
    if self.boredom < 0:
        self.boredom = 0
    self.__pass_time()

def main():

    print("Cars starting")
    car1 = Car("Car №1")
    car2 = Car("Car №3")
    car3 = Car("Car №3")

    Car.status()

    print("Object property acess:", car1.mood)

main()