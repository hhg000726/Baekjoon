import sys
from functools import lru_cache

N, root = list(map(int, sys.stdin.readline().split()))
weights = list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(N)]

for i in range(N - 1):
  a, b = list(map(int, sys.stdin.readline().split()))
  if weights[a - 1] < weights[b - 1]:
    tree[a - 1].append(b - 1)
  else:
    tree[b - 1].append(a - 1) 

@lru_cache(maxsize=None)
def f(index, nearestParent):
  normalSum = weights[index] - weights[nearestParent]
  specialSum = weights[index]
  for c in tree[index]:
    normalSum += f(c, nearestParent)
    specialSum += f(c, index)
  return min(normalSum, specialSum)

print(sum([f(i, root - 1) for i in tree[root - 1]]) + weights[root - 1])