
person = "Bill", "Gates", "Microsoft", "1955-10-24"

print(person[0], person[1], len(person))

first_name, last_name, product, dob = person

values = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

a, *b, c, d, e = values
print(a, b, c, d, e)

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

print(people[0])
print(people[0][0])
print(people[0][0][0])
print()

# for v1, v2, v3 in some_iterable:
#     # v1, v2, v3 = next value of some_iterable

for first_name, last_name, product, dob in people:
    print(first_name, last_name)


def minmax(x):
    return min(x), max(x)

print(minmax([5, 8, 1, 14, 3, -10, 9, 6]))

minimum, maximum = minmax([5, 8, 1, 14, 3, -10, 9, 6])
print(minimum, maximum)

days = 3239

years, days = divmod(days, 365)
print(years, days)




