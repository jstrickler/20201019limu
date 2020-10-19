from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Person:
    PERSON_COUNT: ClassVar = 0  # <.>
    first_name: str  # <.>
    last_name: str

    def __post_init__(self):
        Person.PERSON_COUNT += 1  # <.>

    @classmethod
    def get_census(cls):
        return cls.PERSON_COUNT  # <.>


if __name__ == '__main__':
    p1 = Person('Guido', 'Van Rossum')
    p2 = Person('Larry', 'Wall')
    p3 = Person('Gates', 'Bill')
    print(Person.get_census())  # <.>
