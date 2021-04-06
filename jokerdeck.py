from carddeck import CardDeck

class Thing:
    def doit(self):
        print("doit!!")

class JokerDeck(Thing, CardDeck):

    def _make_deck(self):
        super()._make_deck()  # call parent method
        for num in "1", "2":
            card = (num, "Joker")
            self._cards.append(card)

class PartA:
    pass

class PartB:
    pass

class PartC:
    pass

class X(PartA, PartB):
    pass

class Y(PartB, PartC):
    pass
