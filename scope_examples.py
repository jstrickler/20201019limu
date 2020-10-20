import sys
from typing import Callable

# def print(*args, sep=' ', end='\n'):
#     upper_args = [str(arg).upper() for arg in args]
#     for arg in upper_args[:-1]:
#         sys.stdout.write(arg + sep)
#     sys.stdout.write(upper_args[-1] + end)

x = 100   # global variable
y = "NOT"

def spam():
    x = "SPOT"
    y = 42   # local variable (only visible inside spam
    print(x, y)


spam()

print("in main: x is", x)

x = 5
if x > 0:
    if x > 2:
        if x > 4:
            name = "Bob"

print("Name is", name, sep="=====")

def foo():
    color = 'blue'

    def bar():
        print("color is:", color)  # color is nonlocal

    return bar

f = foo()
f()
import inspect

class Foo:
    pass

f = Foo()  # create instance by "calling" class

def paint(get_color_func: Callable):
    color = get_color_func()
    print("painting it", color)

def blu():
    return "blue"

def pnk():
    return "pink"

paint(blu)
paint(pnk)
# paint(MUST_BE_A_CALLABLE_HERE)

def make_color_func(color):

    def tmp():
        return color

    return tmp

grn = make_color_func("green")
blk = make_color_func("black")

paint(grn)
paint(blk) # rolling stones


def a():
    return 42

print(a)
print(a())

# a is function itself  (does not call code)
# a(...) is function's return value  (calls code)



















