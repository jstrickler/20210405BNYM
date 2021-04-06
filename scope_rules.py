import sys

x = 10  # GLOBAL

def print(*args):
    # sys.stdout.write("HA HA HA\n")
    for arg in args[:-1]:
        sys.stdout.write(str(arg).upper() + ' ')
    sys.stdout.write(str(args[-1]).upper() + '\n')

if x > 5:
    name = 'Fred'  # name is GLOBAL

def spam():
    y = 500  # LOCAL name
    return 42

print("x: {}\n".format(x))
print("spam(): {}\n".format(spam()))
# print("y: {}\n".format(y))

def ham(a, b):
    pass

count = 0  # global count

def incr_count():
    count = 1000  # local count

incr_count()
incr_count()

print("in main(): count:", count)
name = 'Fred'

def aaa():
    name = 'Bob'  # name is local
    print("in aaa(): name is", name)

    def bbb():
        name = "Ravi"
        m = 'mongoose'  # local
        print("in bbb(): name is", name)  # name is nonlocal

        def ccc():
            print("triple nesting!!")
            print(f"in ccc(): name is {name} m is {m}")
        return ccc

    return bbb

f = aaa()
f2 = f()  # calling function bbb() which can "see"  name in aaa()
f2()
print("in main: name is", name)

# print(dir(__builtins__))

__builtins__.print('this is weird')












