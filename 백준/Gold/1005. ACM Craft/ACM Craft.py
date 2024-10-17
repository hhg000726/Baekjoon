import sys
from functools import cache

sys.setrecursionlimit(10001)
T = int(sys.stdin.readline())
for _ in range(T):
    N, k = map(int, sys.stdin.readline().split())
    delays = [0] + list(map(int, sys.stdin.readline().split()))
    parent = dict()
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        if b in parent:
            parent[b].append(a)
        else:
            parent[b] = [a]
    w = int(sys.stdin.readline())
    
    @cache
    def func(n):
        global delays
        global parent
        if n not in parent:
            return delays[n]
        x = 0
        for i in parent[n]:
            x = max(x, delays[n] +func(i))
        return x
                
    print(func(w))