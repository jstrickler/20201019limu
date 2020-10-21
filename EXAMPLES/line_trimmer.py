#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')  # <1>


for trimmed_line in trimmed('../DATA/mary.txt'):  # <2>
    print(trimmed_line)
print()

t = trimmed('../DATA/mary.txt')
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print()


t = trimmed('../DATA/mary.txt')

while True:
    my_iterator = iter(t)
    try:
        trimmed_line = next(my_iterator)
        print(trimmed_line)
    except StopIteration:
        break
