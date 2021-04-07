x = 5

def spam():
    animal = 'wombat'
    print(locals())
name = "Filbert"

g = globals()
print(g)
print(g['name'], g['x'])
g['color'] = "blue"
print(color)

g['bark'] = lambda : print("woof woof")
bark()
print()
spam()
