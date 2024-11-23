class Car:

    def __init__(self, name, hunger = 0, boredom =0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    
    def talk(self):
        print("Wroom Wroom, self.name")

def main():
    car1 = Car("Wroooom stututututu")
    car1.talk()
    car2 = Car("Wroooom Wroooom Wroo00oo00m")
    car2.talk()
    print("Attribute access -", car2.name)
    print(car2)

main()