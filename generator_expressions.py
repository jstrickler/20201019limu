
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

print(len(f1))
print(f1[0], f1[-1])
print()

fgen1 = (f.upper() for f in fruits)
print(fgen1)
# print(len(fgen1))
# print(fgen1[0])

fruits.append("durian")
fruits.append("marionberry")

for fruit in fgen1:
    print(fruit)
print("\n")


fgen2 = (f.upper() for f in fruits)
results1 = list(fgen2)
results2 = list(fgen2)
print("results1:", results1)
print("results2:", results2)

fgen3 = (f.upper() for f in fruits)
for i, fruit in enumerate(fgen3):
    print(fruit)
    if i == 10:
        break
print("------")
for fruit in fgen3:
    print(fruit)
print()

fgen4 = (f.upper() for f in fruits)
f1 = next(fgen4)
f2 = next(fgen4)
print(f1, f2)
