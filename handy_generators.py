from itertools import zip_longest

colors = ['red', 'purple', 'pink', 'green', 'black']
things = ['baron', 'haze', 'panther']

rcolors = reversed(colors)
print(rcolors)
for color in rcolors:
    print(color)
print()

e1 = enumerate(colors)
for i, color in e1:
    print(i, color)
print()
print(list(enumerate(colors)))
print()

combos = zip(colors, things)
print(list(combos), '\n')

for color, thing in zip(colors, things):
    print(color, thing)
print()

for color, thing in zip_longest(colors, things, fillvalue="WOMBAT"):
    print(color, thing)
print()
