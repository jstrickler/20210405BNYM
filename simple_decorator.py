
def bark(old_function):
    def new_function():
        print("Woof! Woof!")
        old_function()
    return new_function

def hello():
    print("Hello, BNYM world")

b = bark(hello)

hello()
print("-" * 60)
b()
print("-" * 60)

hello = bark(hello)
hello()
print("-" * 60)

@bark
def spam():
    print("SPAM SPAM SPAM")
spam()
# spam = bark(spam)