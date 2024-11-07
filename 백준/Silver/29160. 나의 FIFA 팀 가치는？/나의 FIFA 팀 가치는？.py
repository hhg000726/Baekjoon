import sys
import heapq 

N, K = list(map(int, sys.stdin.readline().split()))
heapdict = dict()
answer = 0

for _ in range(N):
    Pi, Ki = list(map(int, sys.stdin.readline().split()))
    if Pi in heapdict:
        heapq.heappush(heapdict[Pi], -Ki)
    else:
        heapdict[Pi] = [-Ki]

for _ in range(K):
    for Pi in heapdict:
        t = min(heapq.heappop(heapdict[Pi]) + 1, 0)
        heapq.heappush(heapdict[Pi], t)

for Pi in heapdict:
    answer += heapq.heappop(heapdict[Pi])

print(-answer)