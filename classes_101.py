from datetime import date

james_bd = date(2014, 8, 1)
susan_bd = date(1948, 5, 23)
print(type(date), type(james_bd))
print(james_bd.toordinal())

name = 'Ravi'   # String name = new String('Ravi');
name = str('Ravi')  # redundantly redundant
print(name.upper())

class Dog:
    def bark(self):
        print("Woof woof")

d1 = Dog()
d2 = Dog()
d3 = Dog()
for d in d1, d2, d3:
    d.bark()






