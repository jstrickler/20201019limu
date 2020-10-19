#!/usr/bin/env python
from collections import namedtuple

person = ['Joe', 'Schmoe', 'Schenectady', 'NY']  # <1>
print("list:", person[0], person[1], "repr:", repr(person))

person = 'Joe', 'Schmoe', 'Schenectady', 'NY'  # <2>
print("tuple:", person[0], person[1], "repr:", repr(person))

person = {'first_name': 'Joe', 'last_name': 'Schmoe', 'city': 'Schenectady', 'state': 'NY'}  # <3>
print("dict:", person['first_name'], person['last_name'], "repr:", repr(person))

Person = namedtuple('Person', 'first_name last_name city state')  # <4>
person = Person('Joe', 'Schmoe', 'Schenectady', 'NY')  # <5>
print("named tuple:", person.first_name, person.last_name, "repr:", repr(person))

class Person:  # <6>
    def __init__(self, first_name, last_name, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state

    def __repr__(self):  # <7>
        return f"Person(first_name='{self.first_name}', last_name='{self.last_name}', city='{self.city}', state='{self.state})"

person = Person('Joe', 'Schmoe', 'Schenectady', 'NY')  # <8>
print("class:", person.first_name, person.last_name, "repr:", repr(person))
