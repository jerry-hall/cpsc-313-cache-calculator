from collections import deque

# Paste input here #
INPUT = "	D,G,B,D,C,C,C,C,G,D,B,G,A,D,C,G,E,G,D,B"
####################

dq = deque()
INPUT = INPUT.lstrip().split(",")
hits = 0
misses = 0
lfu = {}

for i in INPUT:

    if i in dq:
        hits += 1
        dq.remove(i)
        dq.append(i)
        
    else:
        if len(dq) == 4:
            priority = sorted([(a,b) for a, b in lfu.items() if a in dq], key=lambda x: x[1])
            lowest_priority = [a for a, b in priority if b == priority[0][1]]
            dq.remove([a for a in dq if a in lowest_priority][0])
        dq.append(i)
        misses += 1
    
    lfu[i] = lfu.setdefault(i, 0) + 1


print("hits - {}".format(hits))
print("misses - {}".format(misses))