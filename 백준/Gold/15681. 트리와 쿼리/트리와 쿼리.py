import sys
sys.setrecursionlimit(10**6)
N, R, Q = list(map(int, sys.stdin.readline().split()))
Nodes = [0]

class Node:
  def __init__(self, val):
    self.val = val
    self.childs = set()
    self.counts = 1

  def count(self):
    for i in self.childs:
      self.counts += Nodes[i].count()
    return self.counts


for i in range(1, N + 1):
  Nodes.append(Node(i))

for _ in range(N - 1):
  a, b = list(map(int, sys.stdin.readline().split()))
  Nodes[a].childs.add(b)
  Nodes[b].childs.add(a)

q = [R]

while q:
  t = q.pop(0)
  for i in Nodes[t].childs:
    Nodes[i].childs.remove(t)
    q.append(i)

Nodes[R].count()

Queries = []

for _ in range(Q):
  Queries.append(int(sys.stdin.readline()))

for i in Queries:
  print(Nodes[i].counts)