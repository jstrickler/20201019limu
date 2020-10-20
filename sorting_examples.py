
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1:", f1, "\n")

def ignore_case(fruit):
    return fruit.lower()

f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=str.lower)
print("f3:", f3, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("n1:", n1, '\n')

#   i1 > i2

# stuff = [1, 2, "abc", 8, 6, -10, "def", 14, "ccc"]
# print(sorted(stuff))

f4 = sorted(fruits, key=len)
print("f4:", f4, '\n')

def custom_sort(f):
    return len(f), f.lower()

f5 = sorted(fruits, key=custom_sort)
print("f5:", f5, '\n')

# print(f"{f5=}\n")  3.9+

f6 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print("f6:", f6, '\n')

#  min(iter, key=keyfunc)  max(iter, key=keyfunc)








