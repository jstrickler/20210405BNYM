from ANSWERS.president import President

p = President(26)
print(p)
print(p.first_name, p.last_name, p.party)
field_names = "first_name", "last_name"
for field_name in field_names:
    print(field_name, getattr(p, field_name))
print()
print(dir(p))
p.hello()
for func in 'hi', 'hello', 'howdy', 'hiya':
    if hasattr(p, func):
        f = getattr(p, func)
        f()
        break
else:
    raise TypeError("no function found")

def fn(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, 'full_name', fn)

print("my name is", p.full_name())

# delattr(p, 'party')
# print(dir(p))
# print(p.party)



