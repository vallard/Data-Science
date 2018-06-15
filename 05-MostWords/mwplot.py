#!/usr/bin/env python
from matplotlib import pyplot as plt
import sys

counts = []
words = []

try: 
    file_name = sys.argv[1]
except:
    print("enter the file you want to read.")
    sys.exit(1)
    

with open(file_name, 'r') as f:
    for line in f:
        w, c = line.split("\t")
        counts.append(c)
        words.append(w.strip())
plt.pie(counts, labels=words)
plt.show()
