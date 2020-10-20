
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Andy")

print(type(d1))

# d1.shuffle()
# d1.draw()

print(d1.dealer)
d1.dealer = "Nellie"

print(d1.dealer)

try:
    d1.dealer = 5.8
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

d1.shuffle()
print(d1.cards, '\n')

for i in range(7):
    card = d1.draw()
    print(card.rank, card.suit)

# print(x)
# print(str(x))

print(d1.get_suits())
print(CardDeck.get_suits())

d2 = CardDeck("Frodo")
d3 = CardDeck("Rosie")
d4 = CardDeck("Seamus")

print(CardDeck.get_count())
print(d1.get_count())

print(CardDeck.add(10, 5))
print('-' * 60)

j1 = JokerDeck("Fred")
print(j1)
j1.shuffle()
print(j1.cards)
print(j1.get_strategy())

print(JokerDeck.mro())
print(j1.get_it())

print(len(d1), len(j1))

print(d1)
print(j1)
print()

print(repr(d1))
print(repr(j1))

d2 = d1 + j1
print(d2, len(d2))
