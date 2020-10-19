
# mary_in = open(...)

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    whole_enchilada = mary_in.read()
    print("RAW:")
    print(repr(whole_enchilada))
    print("NORMAL:")
    print(whole_enchilada)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print("-" * 60)

print(type(mary_in))
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruitlist.txt', 'x') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

