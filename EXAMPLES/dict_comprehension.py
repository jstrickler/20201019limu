#!/usr/bin/env python
import os

animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']

d = {a.lower(): len(a) for a in animals}  # <1>

print(d, '\n')

file_names = ['../DATA/alice.txt', '../DATA/mary.txt', '../DATA/parrot.txt']

file_sizes = {os.path.basename(fn): os.path.getsize(fn) for fn in file_names}
print("file_sizes:", file_sizes, '\n')

# nested dictionary comprehensions!

words = ['unicorn', 'stigmata', 'barley', 'bookkeeper']

# a little convoluted, but fun:
d = {w:{c:w.count(c) for c in sorted(w)} for w in words} # <2>

for word, word_signature in d.items():
    print(word, word_signature)
print()

# equivalent to:
all_counts = {}
for word in words:
    counts = {}
    for c in sorted(word):
        counts[c] = word.count(c)
    all_counts[word] = counts

for word, word_signature in d.items():
    print(word, word_signature)

# facetiously
