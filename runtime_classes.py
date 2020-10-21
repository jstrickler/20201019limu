
class Animal:
    def move(self):
        print("moving...")

class Cat(Animal):

    def speak(self):
        print("meow")


Dog = type('Dog', (Animal,), {'speak': lambda self: print("woof!")})


c = Cat()
c.speak()
c.move()
print()

d = Dog()
d.speak()
d.move()


# root = objectify("foo.xml")
#
# root.presidents.president.get('first_name')

"""
<presidents>
   <president>
       <first_name>George</first_name>
   </president>
</presidents>

"""
