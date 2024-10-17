import sys

N, M = list(map(int, sys.stdin.readline().split()))
r, c, d = list(map(int, sys.stdin.readline().split()))
room = []
for _ in range(N):
    room.append(list(map(int, sys.stdin.readline().split())))
answer = 0
direction = [[0, -1], [1, 0] ,[0, 1] ,[-1, 0]]

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        answer += 1
    if room[r - 1][c] != 0 and room[r][c - 1] != 0 and room[r + 1][c] != 0 and room[r][c + 1] != 0:
        if room[r - direction[d][1]][c - direction[d][0]] != 1:
            r -= direction[d][1]
            c -= direction[d][0]
        else:
            print(answer)
            break
    else:
        d = d - 1
        if d == -1: d = 3
        if room[r + direction[d][1]][c + direction[d][0]] == 0:
            r += direction[d][1]
            c += direction[d][0]