#!/usr/bin/env python
from dataclasses import dataclass

@dataclass   # <1>
class Person:  # <2>
    first_name: str  # <3>
    last_name: str
    city: str
    state: str


if __name__ == '__main__':
    person = Person('Joe', 'Schmoe', 'Schenectady', 'NY')  # <4>
    print("using fields:", person.first_name, person.last_name)
    print("repr:", repr(person))  # <5>
    person.last_name = 'Smith' # <6>
    print("after changing last name:", person)
