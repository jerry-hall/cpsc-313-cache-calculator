from collections import deque

# Paste input here #
INPUT = "	D,D,E,C,C,D,E,A,C,A,B,A,C,C,D,A,B,C,G,C"
####################

dq = deque()
INPUT = INPUT.lstrip().split(",")
hits = 0
misses = 0

for i in INPUT:

    if i in dq:
        hits += 1
        
    else:
        if len(dq) == 4:
            dq.popleft()
        dq.append(i)
        misses += 1
    

print("hits - {}".format(hits))
print("misses - {}".format(misses))