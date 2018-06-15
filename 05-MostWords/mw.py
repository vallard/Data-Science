#!/usr/bin/env python

import os, sys
from collections import Counter

try:
    num_words = int(sys.argv[1])
except:
    print ("how many words do you want? ")
    sys.exit(1)


counter = Counter(word.lower()
        for line in sys.stdin
        for word in line.strip().split()
        if word)

for word, count in counter.most_common(num_words):
    print("{0}\t{1}".format(word, count))
