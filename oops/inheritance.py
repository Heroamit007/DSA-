#Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

#Child Class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Call parent class constructor
        self.breed = breed

dog = Dog("Rocky", "Labrador")
print(dog.name)
print(dog.breed)


    
# d = Dog("Buddy")
# d.eat()
# d.bark()