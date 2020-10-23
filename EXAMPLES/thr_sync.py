#!/usr/bin/env python
from threading import Thread, Event, Lock
import time

a_ready = Event()

stdout_lock = Lock()


class ThreadA(Thread):

    def run(self):  # <2>
        for i in range(50):
            with stdout_lock:
                print("A:", i)
            if (i > 0) and ((i % 10) == 0):
                with stdout_lock:
                    print("A: setting event")
                a_ready.set()  # notify b
            elif (i > 10) and ((i % 5) == 0):
                with stdout_lock:
                    print("A: clearing event")
                a_ready.clear()  # stop notifying b
            time.sleep(.1)
        a_ready.set()  # let b finish


class ThreadB(Thread):

    def run(self):  # <2>
        for i in range(50):
            with stdout_lock:
                print("B:", i)
            a_ready.wait()
            time.sleep(.1)


t_a = ThreadA()
t_b = ThreadB()
t_a.start()
t_b.start()
t_a.join()
t_b.join()
