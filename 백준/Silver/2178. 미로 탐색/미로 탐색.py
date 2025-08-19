import sys

N, M = map(int, sys.stdin.readline().split())

maps = []
q1 = [[0, 0, 0]]

for _ in range(N):
    maps.append(list(map(int, list(sys.stdin.readline()[:-1]))))

while q1:
    x, y, cnt = q1.pop(0)
    if x == N - 1 and y == M - 1:
        print(cnt + 1)
        break
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
            maps[nx][ny] = 0
            q1.append([nx, ny, cnt + 1])