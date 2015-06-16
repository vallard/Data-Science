# Trial 1

Just takes two books and counts words and sees which words are the most common.  See the
blog post: 

http://benincosa.com/?p=3379

To get the word count of each book, this works: 

```
cat ../data/bom.txt | ./mapper.py | sort -k1,1  | ./reduce.py | sort -k2n | tee ../out/results2.txt
```


