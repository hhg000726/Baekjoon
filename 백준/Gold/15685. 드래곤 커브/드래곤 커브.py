import sys

N = int(sys.stdin.readline())

directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
curves = []
answer = 0

maps = [[False for _ in range(101)] for _ in range(101)]

for _ in range(N):
    curves.append(list(map(int, sys.stdin.readline().split())))

for i in curves:
    x, y, d, g = i
    dsave = [d]
    maps[x][y] = True
    x = x + directions[d][0]
    y = y + directions[d][1]
    maps[x][y] = True
    for j in range(g):
        newd = [((i + 2) % 4 - 1) % 4 for i in dsave[::-1]]
        for k in newd:
            x += directions[k][0]
            y += directions[k][1]
            maps[x][y] = True
        dsave += newd

for i in range(100):
    for j in range(100):
        if maps[i][j] and maps[i + 1][j] and maps[i][j + 1] and maps[i + 1][j + 1]:
            answer += 1

print(answer)