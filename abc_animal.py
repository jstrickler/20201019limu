
from abc import ABCMeta, abstractmethod

# Metaclass -> Class
# Class -> instance


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def move(self):
        pass

    def breathe(self):
        pass

class Dog(Animal):
    def move(self):
        pass

d1 = Dog()
d1.move()
d1.breathe()


class DBBase(metaclass=ABCMeta):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def fetch_result(self):
        pass


# db = DBBase()

class Oracle(DBBase, metaclass=ABCMeta):

    @abstractmethod
    def spam(self):
        pass

class MSSQLServer(DBBase):
    pass

class MySQL(DBBase):
    pass

# my = MySQL()

class LibertyOra(Oracle):
    pass

lo = LibertyOra()
