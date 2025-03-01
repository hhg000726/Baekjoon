import sys

N, M = map(int, sys.stdin.readline().split())

sosize = 1
rem = N
cut = 0
while rem > 0:
  if N >= M:
    rem -= sosize * M
    N -= M
  else:
    div = round(rem / M, 15)
    orisosize = sosize
    sosize = round(orisosize % div, 14)
    mok = round(orisosize // div, 14)
    M -= N * mok
    if sosize == 0:
      cut += N * (mok - 1)
    else:
      cut += N * mok
    N -= M
    rem = round(sosize * N, 14)
print(int(cut))