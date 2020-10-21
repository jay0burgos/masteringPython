class Animal():
    def __init__(self):
        print('Animal Created')
    def who_am_i(self):
        print("i am an Animal")
    def eat(self):
        print("i am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self) #calls animal constructor!
        print("Dog Created")

    def who_am_i(self):
        print('I am a dog')