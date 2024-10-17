import sys

N, M = list(map(int, sys.stdin.readline().split()))

prices= []
pack = 987654321
one = 987654321

for _ in range(M):
    p, o = list(map(int, sys.stdin.readline().split()))
    pack = min(pack, p)
    one = min(one, o)

if pack < 6 * one:
    print(min((N // 6) * pack + (N % 6) * one, ((N // 6) + 1) * pack))
else:
    print(one * N)