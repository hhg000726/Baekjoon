import sys

import sys

N = int(sys.stdin.readline())
supers = list(map(int, sys.stdin.readline().split()))

tree = [[] for _ in range(N)]

for i in range(1, N):
  tree[supers[i]].append(i)

def f(index):
  if not tree[index]: return 1
  l = [f(i) for i in tree[index]]
  l.sort(reverse=True)
  for i in range(len(l)):
    l[i] += i
  return max(l) + 1

print(f(0) - 1)