import sys

N, L = list(map(int, sys.stdin.readline().split()))

answer = [-1]


while True:
  d = N / L
  if d + 1 < L // 2 or L > 100:
    break
  if d == N // L:
    if L % 2 != 0:
      answer = [i for i in range(int(d - L // 2), int(d + L // 2) + 1)]
      break
  else:
    if d * 2 == int(d * 2):
      if L % 2 == 0:
        answer = [i for i in range(int(d + 1 - L // 2), int(d + L // 2) + 1)]
        break
  L += 1

print(*answer)