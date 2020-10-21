#!/usr/bin/env python

import re

with open("../DATA/alice.txt") as mary_in:
    s = {w.lower()  for ln in mary_in  for w in re.split(r'\W+', ln) if w} #<1>
print(sorted(s))

food = ['Spam', 'spaM', 'spam', 'spam', 'spam', 'spam', 'HAM',
        'spam', 'spam', 'SPAM', 'spam', 'Spam', 'Ham', 'ham']

unique_food = {w.lower() for w in food}
print(unique_food)

semi_unique_food = set(food)
print(semi_unique_food)
