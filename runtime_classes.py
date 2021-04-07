s = "hello"
print(type(s))

def bark(self):
    print("Arf Arf Arf ARF ARF")

Dog = type('Dog', (), {'bark': bark, 'fetch': lambda self: print("fetching...")})
d = Dog()
d.bark()
d.fetch()

# class Dog:
#     def fetch(self): pass
#     def bark(self): pass
#