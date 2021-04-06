from carddeck import CardDeck
from jokerdeck import JokerDeck
c1 = CardDeck("Srinivas")
print(c1, type(c1))
# naughty
# print(c1._dealer)
print(c1.dealer)
# print(c1.get_dealer())
c1.dealer = "Ravi"
print(c1.dealer)

try:
    c1.dealer = 12.34
except TypeError as err:
    print(err)

print(c1.dealer)

c2 = CardDeck("1234")
print(c2.dealer)

d = c1.get_dealer()
d = CardDeck.get_dealer(c1)
dd = c2.get_dealer()
# c3.get_dealer()

print(c2.get_dealer())
print("c1:", c1)
c1.doit("up", "down")
print("c2:", c2)
c2.doit("yes", "no")

print(CardDeck.SUITS)
print(c1.get_suits())
print(CardDeck.get_suits())

c1.shuffle()
print(c1.cards, '\n')

for i in range(7):
    print(c1.draw())
print()

j1 = JokerDeck('Anushka')
j1.shuffle()
print(j1.cards)
for i in range(3):
    print(j1.draw())

print(JokerDeck.mro())
j1.doit()
print(len(c1), len(j1))

# print(CardDeck.__len__(c1))

print(c1)  # print(str(c1))
print(j1)
print(repr(c1))
print(repr(j1))
x = c1 + j1
print(x)
print(repr(x))




