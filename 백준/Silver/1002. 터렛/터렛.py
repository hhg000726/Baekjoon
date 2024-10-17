import sys
N = int(sys.stdin.readline())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
        if d > r1 + r2:
            print(0)
        elif d == r1 + r2:
            print(1)
        elif d == abs(r1 - r2):
            print(1)
        elif d < abs(r1 - r2):
            print(0)
        else:
            print(2)