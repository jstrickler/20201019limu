
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')




def doubleit(s):
    return s * 2

f2 = [doubleit(f) for f in fruits]
print("f2:", f2, '\n')

f3 = [f.upper() for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

f4 = [f.upper() for f in fruits if 'p' in f]
print("f4:", f4, '\n')

f5 = [f for f in fruits if f.startswith('p')]
print("f5:", f5, '\n')

nums = [3, 1000, 98, 400, 15, 1729, 8, 45]
n1 = [n for n in nums if n > 100]
print("n1:", n1, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

powers = [(i, i**2, i**3) for i in range(10)]
print("powers:", powers, '\n')

with open('DATA/mary.txt') as mary_in:
    lines = [line.rstrip() for line in mary_in]
print("lines:", lines)




