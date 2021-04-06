import sys
# from pkg.pkg import module
from john.misc import johnlib

johnlib.spam()
johnlib.ham()
print(johnlib.ANIMALS[0])
print()

for path in sys.path:
    print(path)
