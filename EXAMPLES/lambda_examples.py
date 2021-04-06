#!/usr/bin/env python

fruits = ['watermelon', 'Apple', 'Mango', 'KIWI', 'apricot', 'LEMON', 'guava']

sorted_fruits = sorted(fruits, key=lambda e: e.lower())  # <1>

print(" ".join(sorted_fruits), '\n')

f = sorted(fruits, key=lambda fruit: (len(fruit), fruit.lower()))
print(f)