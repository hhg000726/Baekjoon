import sys

N = int(sys.stdin.readline())
maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
state = 2
left = 2
time = 0

for i in range(N):
    for j in range(N):
        if maps[i][j] == 9:
            x = i
            y = j

while True:
    close = [-1, -1]
    ttime = 1000
    q = [[x, y, 0]]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    while q:
        t = q.pop(0)
        for i in dir:
            tx = t[0] + i[0]
            ty = t[1] + i[1]
            tcount = t[2] + 1
            if -1 < tx < N and -1 < ty < N:
                if maps[tx][ty] <= state and visited[tx][ty] == False:
                    visited[tx][ty] = True
                    q.append([tx, ty, tcount])
                    if 0 < maps[tx][ty] < state:
                        if tcount < ttime or (tcount == ttime and close[0] > tx) or (tcount == ttime and close[0] == tx and close[1] > ty):
                            close = [tx, ty]
                            ttime = tcount
    if ttime == 1000:
        print(time)
        break
    else:
        maps[x][y] = 0
        maps[close[0]][close[1]] = 9
        x, y = close[0], close[1]
        left -= 1
        if left == 0:
            state += 1
            left = state
        time += ttime