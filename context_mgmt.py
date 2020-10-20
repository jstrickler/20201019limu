from abc import ABCMeta, abstractmethod

with open('DATA/mary.txt') as mary_in:
    pass


class DBBase(metaclass=ABCMeta):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass


class OracleDB(DBBase):

    def connect(self):
        print("Connecting...")


    def close(self):
        print("Closing")

    def __enter__(self):
        print("Entering...")
        return self.connect()

    def __exit__(self, *exc):
        print("Exiting...")
        self.close()


with OracleDB() as ora:
    print("Working on DB")

print("All done")
