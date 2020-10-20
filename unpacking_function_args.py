
def doit(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)


doit(1, 2, 3)

values = [4, 5, 6]

# doit(values)
#     won't work

doit(*values)

def config(**kwargs):
    print(kwargs)

config(filename='mary.txt', folder="DATA", factor=3.5)

values = {
    'filename': 'alice.txt',
    'factor': 2.9,
    'folder': 'BIGDATA',
}

config(**values)
