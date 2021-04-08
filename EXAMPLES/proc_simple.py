#!/usr/bin/env python
from multi_processing import Process, Manager
import random
import time


class SimpleThread(Process):
    def __init__(self, num):
        super().__init__()  # <1>
        self._threadnum = num

    def run(self):  # <2>
        time.sleep(random.randint(1, 3))
        print("Hello from process {}".format(self._threadnum))

if __name__ == '__main__':
    manager = Manager()
    values = manager.list() # pseudo-list
    stuff = manager.dict()  # pseudo-dict
    for i in range(10):
        t = SimpleThread(i)  # <3>
        t.start()  # <4>

    print("Done.")
