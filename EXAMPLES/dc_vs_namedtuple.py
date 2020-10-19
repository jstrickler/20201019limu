#!/usr/bin/env python
from collections import namedtuple
from dataclasses import make_dataclass, asdict, fields


field_names = ['x', 'y']   # <.>
field_types = [int, int]   # <.>

PointNT = namedtuple('PointNT', field_names)  # <.>

pnt1 = PointNT(5, 10)  # <.>
print(pnt1, pnt1.x, pnt1.y)  # <.>

# dataclass
PointDC = make_dataclass('PointDC', zip(field_names, field_types), order=True)  # <.>

pdc1 = PointDC(5, 10)  # <.>
print(pdc1, pdc1.x, pdc1.y)  # <.>

print()

pnt2 = PointNT(10, 20)  # <.>

pdc2 = PointDC(10, 20)

print(pnt2 > pnt1)  # <.>
print(pdc2 > pdc1)

print(pnt1._asdict())  # <.>
print(asdict(pdc2))

print(pnt1._fields)  # <.>
print("----")
for f in fields(pdc1):
    print(f)

print()

for p in pnt1, pdc1:  # <.>
    try:
        p.x = 100
    except AttributeError as err:
        print(err)
    else:
        print(p)
