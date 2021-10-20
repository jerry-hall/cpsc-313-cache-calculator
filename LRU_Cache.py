from collections import deque

# Paste input here #
INPUT = "	G,D,G,G,D,B,C,G,E,D,E,G,A,D,G,A,B,A,G,E"
####################

dq = deque()
INPUT = INPUT.lstrip().split(",")
hits = 0
misses = 0

for i in INPUT:

    if i in dq:
        hits += 1
        dq.remove(i)
        dq.append(i)
        
    else:
        if len(dq) == 4:
            dq.popleft()
        dq.append(i)
        misses += 1
    

print("hits - {}".format(hits))
print("misses - {}".format(misses))