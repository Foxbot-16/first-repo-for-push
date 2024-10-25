# python classes and inheritance

class Animal():
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# create a class that inheritance from the Animal class
class Dog(Animal):
    def speak(self):
        print("WOOF!")
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

# create an object named dog calling the dog CONSTRUCTOR
dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

# even if the children classes are empty we can still work with the parent
# makes the code more flexiable
print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

# print the speak function inside the dog child
dog.speak()