#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)

arr_size = 3
a = []

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        w = ''.join(e for e in word if e.isalnum())
        a.append(w.lower())
        if len(a) > arr_size:
          a.pop(0) 
        if len(a) > arr_size - 1:
          print '%s\t%s' % (' '.join(aa for aa in a), 1)
