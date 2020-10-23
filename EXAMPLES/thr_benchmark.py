#!/usr/bin/env python

from timeit import Timer
import random

with open('../DATA/words.txt') as words_in:
    WORDS = [w.strip() for w in words_in]

random.shuffle(WORDS)

setup = """
from __main__ import WORDS
"""

sequential = """
WORD_LIST = [w.upper() for w in WORDS]
"""

multi_threaded = """
from multiprocessing.dummy import Pool
POOL_SIZE = 10

def my_task(word):
    return word.upper()

tpool = Pool(POOL_SIZE)

WORD_LIST = tpool.map(my_task, WORDS)

del(tpool)
"""

t1 = Timer(stmt=sequential, setup=setup)
t2 = Timer(stmt=multi_threaded, setup=setup)

print(t1.timeit(100))
print(t2.timeit(100))
