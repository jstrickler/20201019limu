import typing as T


name: str

name = 4.2

FloatOrInt = T.Union[int, float]

class Person:
    pass



Persons = T.Iterable[Person]

def get_last_name(persons: Persons):
    pass

def get_average(a: FloatOrInt, b: FloatOrInt) -> float:
    return (a + b) / 2   # PEMDAS

result: float = get_average(5, 10)
print(result)

# result = get_average('a', 'b')
# print(result)

result = get_average(1.2, 3.9)
print(result)

print("name is", name)

print(get_average.__annotations__)


class Spam:
    def ham(self, thing: 'Eggs'):
        pass

class Eggs:
    def toast(self, thing: Spam):
        pass

s = Spam()
e = Eggs()
s.ham(e)
e.toast(s)

def Blurb(x: T.List[str]) -> T.List[str]:
    return ['s']

#  dict set list tuple

def Flurp(x: T.List[Spam]):
    pass

def Gorg(x: T.Dict[str, T.List[T.Union[Eggs, Spam]]]):
    pass

def bloop(x: T.Any) -> T.NoReturn:
    pass

def flarf(x: T.Iterable):
    print(x)


r = range(25)

flarf(r)
flarf('abc')
flarf(b'abc')
flarf([1, 2, 3])
flarf((1, 2, 3))
flarf({'a': 1, 'b': 2})
flarf({1, 2, 3})  # set
flarf(123)
flarf(s)
flarf(1.23)

def fimoo(x: T.Optional[str]=None):
    pass

fimoo('abc')
fimoo()

#  T.Optional[x]  == T.Union[x, None]

