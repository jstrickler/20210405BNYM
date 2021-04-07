"""
Provide CardDeck class
"""
import random

class CardDeck:  # inherits from object
    """
    Represent one deck of cards.
    """
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    @classmethod
    def get_suits(cls):
        # no access to instance data
        return cls.SUITS

    def __init__(self, dealer):
        """
        Constructor

        :param dealer: Dealer name as string
        """
        self.dealer = dealer
        self._make_deck()


    def _make_deck(self):
        self._cards = list()
        # (rank, suit)
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)


    def cards(self):
        return self._cards
    cards = property(cards)  # same as using @property


    @property  # decorator
    def dealer(self):  # getter property
        # called when X.dealer is evaluated
        return self._dealer

    @dealer.setter
    def dealer(self, new_dealer): # setter property
        # called when X.dealer is assigned to
        if isinstance(new_dealer, str):
            self._dealer = new_dealer
        else:
            raise TypeError('Dealer must be a string')


    # dealer = property(dealer)
    def get_dealer(wombat):
        return wombat._dealer

    def doit(self, a, b):
        print("self:", self)
        print("a:", a)
        print("b:", b)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    #   CardDeck<DEALER, CARDSLEFT>
    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name} <{self.dealer}, {len(self)}>"

    def __repr__(self):
        # how to create object
        # CardDeck("dealer name")
        my_type = type(self)
        my_name = my_type.__name__
        return f'{my_name}("{self.dealer}")'

    def __add__(self, other):
        my_type = type(self)
        tmp = my_type(self.dealer)
        tmp._cards = self._cards + other._cards
        return tmp