import sys

N = int(sys.stdin.readline())
guilty = list(map(int, sys.stdin.readline().split()))
R = []
for _ in range(N):
  R.append(list(map(int, sys.stdin.readline().split())))
me = int(sys.stdin.readline())
answer = 0

mem = set()

if N % 2 == 1:
  maxG = max(guilty)
  guilty[guilty.index(maxG)] = -1000

def f(guilty, t):
  if tuple(guilty) in mem:
    return
  mem.add(tuple(guilty))
  global answer
  if guilty[me] == -1000:
    answer = max(answer, t)
  else:
    ori_guilty = guilty.copy()
    for i in range(N):
      if i == me or guilty[i] == -1000: continue
      else:
        guilty[i] = -1000
        for j in range(N):
          if guilty[j] != -1000:
            guilty[j] += R[i][j]
        maxG = max(guilty)
        guilty[guilty.index(maxG)] = -1000
        f(guilty, t + 1)
        guilty = ori_guilty.copy()

f(guilty, 0)

print(answer)