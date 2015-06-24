# Most common phrases
After word count, we'd like to see what the most common phrases are that people are saying. 
We won't be tricky, we'll just match like for like strings, ignoring case.  

## Thought 1:
Go through the text and take every 3 words and put a one by them. 
Reduce this and see which ones have more than 3 the same.  

Next we can iterate through the text again, taking only the more than
3 phrases and see which ones have 4.  

We can then iterate like this until we run out of exact phrases that are the 
same.  

We could then plot this to see how much of a work (or book) is repetitive and how much of 
the content is actually new.  Might be fun!

Run the command like: 

```
cat ../data/bom.txt | ./mapper.py | sort -k1,1 | ./reduce.py | sort -kXXn | tee ../out/results1.txt

(where XX is the number of touple you are looking for plus 1.)
```
