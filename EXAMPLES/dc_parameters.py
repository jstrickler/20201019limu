from dataclasses import dataclass

@dataclass
class PublishedDateIncomparable():  # <.>
    year: int
    month: int
    day: int

p1 = PublishedDateIncomparable(2020, 10, 31)  # <.>
p2 = PublishedDateIncomparable(2020, 9, 22)

print("Incomparable:", end=' ')
try:
    result = p1 > p2  # <.>
except TypeError as err:
    print(err)
else:
    print(result)

@dataclass(order=True)  # <.>
class PublishedDateComparable:
    year: int
    month: int
    day: int

p1 = PublishedDateComparable(2020, 10, 31)
p2 = PublishedDateComparable(2020, 9, 22)

print("Comparable:", end=' ')
try:
    result = p1 > p2  # <.>
except TypeError as err:
    print(err)
else:
    print(result)
