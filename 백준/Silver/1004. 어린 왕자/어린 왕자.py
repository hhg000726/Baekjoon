import sys
T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    pos = []
    for _ in range(N):
        pos.append (list(map(int, sys.stdin.readline().split())))
    count = 0
    for i in pos:
        if ((x1 - i[0]) ** 2 + (y1 - i[1]) ** 2 < i[2] ** 2) ^ ((x2 - i[0]) ** 2 + (y2 - i[1]) ** 2 < i[2] ** 2):
            count += 1
    print(count)