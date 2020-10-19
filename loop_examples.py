i = 0
while i < 3:
    print(i)
    i += 1
print()

# while True:
#     request = input("Word to look up: ")
#     if request == 'q':
#         break
#     if request == '':
#         continue
#     print(f"Looking up {request}")
# print()

items = ['axe', 'kitten', 'table']

for item in items:
    print(item)
print()

for i in range(5):
    print(i)
print()


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

target = 'z'

for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print("{} not found".format(target))



