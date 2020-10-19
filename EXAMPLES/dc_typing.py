#!/usr/bin/env python
import sys
from dataclasses import dataclass, field
from typing import List, Dict, Any, Union  # <.>
from datetime import date

@dataclass
class PhoneNumber:  # <.>
    number: str  # <.>

@dataclass()
class AddressBookEntry:
    title: Union[str, None]  # <.>
    first_name: str
    middle_name: Union[str, None]
    last_name: str
    phone_numbers: List[PhoneNumber]  # <.>
    # note: as of 3.9, list[PhoneNumber] is valid (also dict, tuple, set, frozenset)
    birthday: date

if __name__ == '__main__':

    p = AddressBookEntry("Mr.", "Bob", "J.", "Smith", [PhoneNumber('919-872-9302')],
                         date(1978, 12, 10))
    print(p)
    print(p.last_name)
    print(p.phone_numbers[0])
    p.phone_numbers.append(PhoneNumber('919-239-7204'))  # <.>
    print(p)

