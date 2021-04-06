
values = 5, 8, 2, 97
actor = 'Chris Hemsworth'

for v in values:
    #  v = next(values)
    print(v)
print()

for char in actor:
    print(char.upper(), end='/')
print()

for i, value in enumerate(values):
    # i, value = <next element of> enumerate(values)
    print(i, value)
print()
print(list(enumerate(values)))

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

target = 'a'

for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break  # break the for loop
else:
    print(target, "not found")