# Cache Hit and Miss Calculator

In CPSC 313: Computer Hardware and Operating Systems, it is asked to calculate the hits and misses of LFU and LRU caches. This project is to calcluate hits/misses.

### Example Question

>Assume you are given a tiny 4-element, fully-associative cache that uses LFU replacement. The cache stores single byte values (i.e., a line is a single byte). In case of a tie, replace the item in the earliest position in the cache (e.g,. if the slots are numbered 0, 1, 2, 3, then in a tie between slots 1 and 3, place the new item in slot 1). If the cache is empty at the beginning of execution, how many hits will the following string of accesses produce?
>
>	    D,G,B,D,C,C,C,C,G,D,B,G,A,D,C,G,E,G,D,B

## Usage
```
-> % python LFU_Cache.py
hits - 13
misses - 7
```