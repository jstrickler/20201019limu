#!/usr/bin/env python

from threading import Thread, Lock
import random
import time

output_lock = Lock()

class SimpleThread(Thread):
    def __init__(self, num):
        super().__init__()  # <1>
        self._threadnum = num

    def run(self):  # <2>
        time.sleep(random.randint(1, 3))
        with output_lock:
            print("Hello from thread {}".format(self._threadnum))


for i in range(10):
    t = SimpleThread(i)  # <3>
    t.start()  # <4>

print("Done.")
