class Car(object):

    def __init__(self):
        print("Авто заводиться")

    def talk(self):
        print("Wroom Wroom Wroooooom stututututu")

def main():
    car1 = Car()
    car1.talk()
    car2 = Car()
    car2.talk()

main()