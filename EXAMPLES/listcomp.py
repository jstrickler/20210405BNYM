#!/usr/bin/env python

fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']

values = [2, 42, 18, 92, "boom", ['a', 'b', 'c']]

ufruits = [f.upper() for f in fruits]  # <1>

afruits = [fruit for fruit in fruits if fruit.startswith('a')]  # <2>

doubles = [v * 2 for v in values]  # <3>

print("ufruits:", " ".join(ufruits))
print("afruits:", " ".join(afruits))
print("doubles:", end=' ')
for d in doubles:
    print(d, end=' ')
print()

food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'nutella', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam',
        'eggs', 'spam', 'spam', 'nutella', 'spam', 'spam', 'toast',
        'spam', 'spam', 'spam', 'spam', 'spam', 'spam', ]

banned_foods = 'spam', 'nutella'
good_food = [f.title() for f in food if f not in  banned_foods]
print(good_food)

SUITS = 'Clubs Diamonds Hearts Spades'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
cards = [(r, s) for s in SUITS for r in RANKS]
print(cards, '\n')

