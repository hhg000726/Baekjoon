import sys

N = int(sys.stdin.readline())
checker = []
x = []
y = []
d = dict()
for i in range(N):
    checker.append(list(map(int, sys.stdin.readline().split())))
    x.append(checker[i][0])
    y.append(checker[i][1])

p = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        p[i][j] = [x[i], y[j]]
        
for i in range(N):
    for j in range(N):
        d[(i, j)] = []
        for k in checker:
            d[(i, j)].append(abs(p[i][j][0] - k[0]) + abs(p[i][j][1] - k[1]))
        d[(i,j)].sort()
        for k in range(len(d[(i, j)]) - 1):
            d[(i, j)][k + 1] += d[(i, j)][k]
        
answer = []
for i in range(N):
    t = 987654321
    for j in range(N):
        for k in range(N):
            t = min(t, d[(j, k)][i])
    answer.append(t)

print(*answer)