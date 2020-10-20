import random
import typing

class Card:
    def __init__(self, rank: str, suit: str):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self) -> str:  # Java: to_string()
        return f'Card({self.rank}, {self.suit})'

# static block here....


class CardDeck:

# Java/C#/Scala/C++:  this
# Python: self

    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    DECK_COUNT = 0

    def __init__(self, dealer: str):
        self._dealer = dealer  # private data
        self._cards: typing.List[Card] = list()
        CardDeck.DECK_COUNT += 1
        self._make_deck()

    def _make_deck(self) -> None:
        """
        Create deck of cards from suits & ranks

        :return: None
        """
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(Card(rank, suit))

    @property
    def length(self):
        return len(self._cards)


    @property
    def cards(self):
        return [str(c) for c in self._cards]

    @property  # decorator
    def dealer(self) -> str:  # getter property
        return self._dealer

    @dealer.setter  # created by getter prop
    def dealer(self, dealer: str) :  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a str")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def add(a, b):  # why am I here?
        return a + b

    @classmethod
    def get_count(cls):
        return cls.DECK_COUNT

    def __len__(self):
        return len(self._cards)

    def __str__(self):  # what am I?
        class_type = type(self)
        class_name = class_type.__name__

        return f"{class_name}({self.dealer}, {len(self)})"

    def __repr__(self):  # how was I created?
        class_type = type(self)
        class_name = class_type.__name__
        return f"""{class_name}("{self.dealer}")"""

    def __add__(self, other):
        class_type = type(self)
        tmp = class_type(self.dealer)
        tmp._cards = self._cards + other._cards
        return tmp

