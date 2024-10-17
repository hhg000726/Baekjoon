import sys

N = int(sys.stdin.readline())
homes = sorted(list(map(int, sys.stdin.readline().split())))

if N % 2 == 0:
    print(homes[int(N / 2) - 1])
else:
    print(homes[int((N - 1) / 2)])