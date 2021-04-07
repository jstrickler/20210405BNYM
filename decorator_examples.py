from datetime import datetime
from collections import Counter
from functools import wraps

call_count = Counter()

def timestamp(orig_func):
    @wraps(orig_func)
    def new_func(*args, **kwargs):
        # log the call
        # count how many times orig_function was called
        print(datetime.now().ctime())
        call_count[orig_func.__name__] += 1
        return orig_func(*args, **kwargs)
    return new_func

@timestamp
def spam():
    print("Hello from spam()")

@timestamp
def ham():
    print("hello from ham()")

spam()
spam()
ham()

@timestamp
def eggs():
    print("hello from eggs()")

for i in range(10):
    eggs()
print()
print(call_count)

# @foo
# def blah():
#     pass
# blah = foo(blah)

@bar('wombat')
# def blah():
#     pass
# blah = bar('wombat')(blah)

def deco_with_params(p1, p2):
    def sub_deco(orig_func):
        @wraps(orig_func)
        def new_func(*args, **kwargs):
            # do your thing here...with p1 and p2....
            return orig_func(*args, **kwargs)
        return new_func
    return sub_deco

@deco_with_params(5, "abc")
def whatever():
    pass