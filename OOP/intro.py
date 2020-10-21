#type control in python    
# 
# 
# 
# Class Object attribute
class Dog():
    species = 'Mammal' #<-- this is a class object attribute!!!

    def __init__(self, breed, name, spots): #<-- these are user defined attrubutes
        self.breed = breed
        self.name = name

    def bark(self): #self connects function to object
        print('Woof') #object method

