# CALLBACKS

# library code -- business logic
def doit(the_function):
    msg = "Update from doit()"
    the_function(msg)

# client code -- interface logic (AKA GUI, UI, UX)
def hello(s):
    print(s.upper())

doit(hello)
