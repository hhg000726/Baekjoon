import sys
import string
from itertools import combinations
N, K = map(int, sys.stdin.readline().split())
words = []
for _ in range(N):
  words.append(set(sys.stdin.readline().split('\n')[0]))
alps = list(string.ascii_lowercase)
pre = ['a', 'c', 't', 'i', 'n']
for ch in pre:
  alps.remove(ch)
for word in words:
  for ch in pre:
    word.discard(ch)
K -= 5
if K >= 0:
  answer = 0
  combs = list(combinations(alps, K))
  for comb in combs:
    s = set(comb)
    t = 0
    for word in words:
      if not word - s:
        t += 1
    answer = max(t, answer)
  print(answer)
else:
  print(0)