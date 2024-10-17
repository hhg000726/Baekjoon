import sys

N = int(sys.stdin.readline())
buildings = list(map(int, sys.stdin.readline().split()))
connect = [[False for _ in range(N)] for _ in range(N)]
answer = 0
for i in range(0, N):
    for j in range(0, N):
        if i == j:
            continue
        m = min(i, j)
        M = max(i, j)
        check = True
        for k in range(m + 1, M):
            if buildings[k] >= (buildings[m] * (M - k) + buildings[M] * (k - m)) / (M - m):
                check = False
                break
        if check:
            connect[i][j] = True

for i in range(N):
    count = 0
    for j in range(N):
        if connect[i][j]:
            count += 1
    answer = max(answer, count)

print(answer)