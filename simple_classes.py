

class Animal:  # (object)

    def move(self):
        print("I am moving...")

a = Animal()
a.move()
print(type(a))

class Dog(Animal):  # Animal is base class

    def __init__(self):   # unrelated to __init__.py
        print("Hi Mom!")

    def bark(self):
        print("Woof! Woof!")


d1 = Dog()   # d1 is instance of Dog
print(type(d1))
d1.move()  # move() and bark() are methods
d1.bark()

print(Dog.mro())
d2 = Dog()
d3 = Dog()

