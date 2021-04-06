
ANIMALS = ['wombat', 'wildebeest', 'wolverine']

def main():
    print("Hi MOM!")
    ham()
    spam()

def spam():
    print("Hello from spam()")

def _toast():
    print("    and _toast()")

def ham():
    print("Hello from ham()")
    _toast()

if __name__ == '__main__':  # if executed, NOT imported
    main()