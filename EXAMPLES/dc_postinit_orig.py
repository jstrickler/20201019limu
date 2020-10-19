#!/usr/bin/env python
from dataclasses import dataclass
from datetime import date

@dataclass()
class ComputerPerson():

    first_name: str
    last_name: str
    organization: str
    birthdate: date
    full_name: field(init=False)

    def __post_init__(self):
        self.full_name = '{} {}'.format(
            self.first_name, self.last_name
        )

p = ComputerPerson(first_name='Bill', last_name='Gates', organization="Microsoft", birthdate=date(1955, 10, 28))

print(p)

print(p.full_name)

