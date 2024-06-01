class Animal:
    animalType = "mammal"


class Pets(Animal):
    color = 'white'


class Dog(Pets):
    
    @staticmethod
    def bark():
        print("bow bow!")


d = Dog()
d.bark()
