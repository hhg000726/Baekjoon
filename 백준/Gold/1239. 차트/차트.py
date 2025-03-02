import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

answer = 0

def f(i, l, numbers):
  if i == N:
    tl = l[::]
    tt = []
    tt.append(tl.pop(0))
    s = tt[0]
    tanswer = 0
    while tl:
      if s == 50:
        global answer
        tanswer += 1
      while s >= 50:
        s -= tt.pop(0)
      while tl and s < 50:
        tt.append(tl.pop(0))
        s += tt[-1]
    global answer
    answer = max(answer, tanswer)
    return
  for j in range(len(numbers)):
    l[i] = numbers[j]
    f(i + 1, l, numbers[:j] + numbers[j + 1:])

f(0, [0 for _ in range(N)], numbers[::])

print(answer)