
from carddeck import CardDeck, Card

class Game():

    def get_strategy(self):
        return "Strategy!"


class JokerDeck(CardDeck, Game):

    def _make_deck(self) -> None:
        super()._make_deck()
        self._cards.append(Card('1', 'Joker'))
        self._cards.append(Card('2', 'Joker'))


    def get_it(self):
        return "it"
