from pprint import pprint

airports = {
    'LAX': 'Los Angeles',
    'RDU': 'Raleigh-Durham',
    'JFK': 'Kennedy',
    'IAD': 'Dulles',
}
print(airports.get('LAX'))
print(airports.get('EWR'))
print(airports.get('EWR', 'NOT FOUND'))
print(airports['IAD'])
airports['ORD'] = "O'Hare"
airports['DIA'] = "Denver"
pprint(airports)
print()
print("airports: {}\n".format(airports))

print(airports.keys())
print(airports.values())
print()

for abbr, name in airports.items():
    print(abbr, name)

print(list(airports.items()))

print(airports.setdefault('SEA', 'Seattle/Tacoma'))
print(airports.setdefault('RDU', 'Durham-Raleigh'))
pprint(airports)

s1 = {'red', 'blue', 'blue', 'blue', 'green', 'purple', 'black', 'brown', 'red'}
s2 = {'black', 'black', 'red', 'green', 'orange', 'blue'}

print(s1)
print(s2)
print()

print(s1 & s2)  # intersection
print(s1 ^ s2)  # xor
print(s1 | s2)  # union
print(s1 - s2)
print(s2 - s1)

s = "Mississippi"
print(set(s))


