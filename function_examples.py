from message_utils import get_message

def print_message():
    message = get_message()
    print(message)

result = print_message()

print(result)

def fix_string(s):
    return s.strip().lower()


print(fix_string("   WoW!   THIS is FuN      "))
print()

def powers(x):
    return x, x ** 2, x ** 3

for i in range(5):
    print(powers(i))
print()


def wacky(p1, p2, *p3, n1, n2, **n3):
    print(p1, p2, p3, n1, n2, n3)

wacky(5, 10, n1=100, n2=200, wombat=300, tarantula=400)
print()

wacky(5, 10, 15, 20, 25, 30, n1=100, n2=200, wombat=300, tarantula=400)
print()

def spam(*, user="root", folder="/"):
    print(user, folder)

spam()
spam(folder='/users/jstrick')
spam(user="bob")
spam(folder='/etc', user="admin")
print()

def eggs(a, b):
    print(a, b)

eggs(5, 10)
eggs(a="big", b="tiny")
eggs(b=['fruitbat'], a="almond")
print()



#  3.9+
# positional-only, positional, optional positional, name-only, optional named

def toast(a, c, *d, e, f, **g):
    print(a, c, d)

toast(a=1, c=5, d=6)

def config(**values):
    print(values)

config(file=2, name=4, cousin="Randy")













