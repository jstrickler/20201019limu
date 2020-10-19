x = 5

y = x
# int x = new int(5)

x = 10 # create new obj and use name 'x' for it

print(x, y)

stuff = [1, 2, 3]

def spam(things):
    print(things)
    things.append('wombat')

spam(stuff)
print(stuff)

items = stuff
print(stuff, items)

items.append('koala')
print(stuff, items)

junk = list(items)
junk.append('platypus')
print(stuff, items, junk)

print(items is stuff)   #  a is b    a == b
print(junk is stuff)
print(id(items), id(stuff), id(junk))

list1 = [['a', 'b', 'c'], ['d', 'e', 'f']]
list2 = list1
list3 = list(list1)
list2.append([1, 2, 3])

print(list1, list2, list3)
list1[0].append('wow!')
print(list1)
print(list2)
print(list3)

from copy import deepcopy
list4 = deepcopy(list1)
list1[1].append("oh boy")

print(list1)
print(list2)
print(list3)
print(list4)

#  _  abc  AbC_12_8_   ALPHA  buttermilk  _1_

_ = 5

print(_ * 10)

maximum_tries = 5

# mutable: list, set, dict
# immutable: everything else

flag = True

stuff = [False, False, False]










