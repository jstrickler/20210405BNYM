actor = 'Chris Hemsworth'
values = [1, 3, 4, 19]

print(len(actor), len(values))
print(actor[0], values[0])
print(min(actor), max(actor), sorted(actor), min(actor.replace(' ','')))
print(min(values), max(values), sorted(values))

print(actor[6:9])

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0:5])
print(fruits[5:10])

print(fruits[:3])
print(fruits[-5:])

for fruit in fruits:
    print(fruit.upper())

#  list, tuple, str, bytes

b = b"abc"
print(b)
print(b[0], b[:2])
print(list(b))