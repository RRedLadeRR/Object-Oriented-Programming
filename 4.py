class Car:

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    
    def __str__(self):
        ans = "Object class Car\n"
        ans += "Country: " + self.name + "\n"
        return ans

def main():
    car1 = Car("Japan")
    car2 = Car("USA")
    print(car2)

main()