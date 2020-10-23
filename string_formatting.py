
name = "Sisi"

company = "Liberty"

value = 2.19 / 27.63

print(name, company, value)

print(name, "works for", company)

# legacy (<= 2.6)
# modern (2.7 and 3.0+)
# fstrings (3.7+)

print("{} works for {}".format(name, company))
print(f"{name} works for {company}")

print("2 + 2 is {}".format(2 + 2))
print(f"2 + 2 is {2 + 2}")

print("value is {}".format(value))
print("value is {:.2f}".format(value))
print(f"value is {value:.2f}")

# s string
# d integer
# f float
# x hex
# b binary
# < right justify
# > left  ^ center
#  width.precisionX
#

factors = 12, 1, 348, 19
people = ['Andy', 'Nellie', 'Frodo', 'Rosie']
colors = 'red blue green purple'.split()


for person, factor, color in zip(people, factors, colors):
    print("{:10s} {:4d} {:>8s}".format(person, factor, color))

big_num = 20394820394820394820934820934820938
print("{:,d}".format(big_num))

for factor in factors:
    print("{0:4d} {0:04x} {0:10b} {0:6o}".format(factor))
