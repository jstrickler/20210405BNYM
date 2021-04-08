#!/usr/bin/env python
from threading import Thread, Lock
import random
import time

VALUES = []

STDOUT_LOCK = Lock()  # generic lock

def d1(a, b, c):
    with STDOUT_LOCK:   # wait until lock is available; acquire lock; release lock
        print("Hi hi hi")

def d2():
    with STDOUT_LOCK:
        print("Ho ho ho")

    # STDOUT_LOCK.acquire()
    # print("Ho ho ho")
    # STDOUT_LOCK.release()



def doit(num):  # <1>
    time.sleep(random.randint(1, 3))
    values = 1, 2, 3
    t_d1 = Thread(target=d1, args=values)
    t_d2 = Thread(target=d2)
    t_d1.start()
    t_d2.start()
    with STDOUT_LOCK:
        print("Hello from thread {}".format(num))


for i in range(10):
    t = Thread(target=doit, args=(i,))  # <2>
    t.start()  # <3>

print("Done.")  # <4>
