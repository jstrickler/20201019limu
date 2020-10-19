from dataclasses import dataclass

@dataclass
class Point:
    x: int = 0.0  # <.>
    y: int = 0.0

p1 = Point()  # <.>
p2 = Point(3.4, 5.8)  # <.>

print(p1, p2)
