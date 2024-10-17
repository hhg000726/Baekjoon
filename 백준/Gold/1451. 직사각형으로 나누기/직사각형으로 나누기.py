import sys

N, M = map(int, sys.stdin.readline().split())
maps = []
psum = [[0 for _ in range(M)] for _ in range(N)]
answer = 0
for i in range(N):
    maps.append(list(map(int, list(sys.stdin.readline()[:-1]))))
    
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            psum[i][j] = maps[i][j]
        elif i == 0:
            psum[i][j] = psum[i][j - 1] + maps[i][j]
        elif j == 0:
            psum[i][j] = psum[i - 1][j] + maps[i][j]
        else:
            psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + maps[i][j]

for i in range(N):
    for j in range(i + 1, N):
        answer = max(answer, psum[i][M - 1] * (psum[j][M - 1] - psum[i][M - 1]) * (psum[N- 1][M - 1] - psum[j][M - 1]))
        
for i in range(M):
    for j in range(i + 1, M):
        answer = max(answer, psum[N - 1][i] * (psum[N - 1][j] - psum[N - 1][i]) * (psum[N- 1][M - 1] - psum[N - 1][j]))
        
for i in range(N - 1):
    for j in range(M - 1):
        answer = max(answer, psum[N - 1][j] * (psum[i][M - 1] - psum[i][j]) * (psum[N- 1][M - 1] - psum[N - 1][j] - psum[i][M - 1] + psum[i][j]), psum[i][M - 1] * (psum[N - 1][j] - psum[i][j]) * (psum[N- 1][M - 1] - psum[N - 1][j] - psum[i][M - 1] + psum[i][j]), psum[i][j] * (psum[i][M - 1] - psum[i][j]) * (psum[N- 1][M - 1] - psum[i][M - 1]), psum[i][j] * (psum[N - 1][j] - psum[i][j]) * (psum[N- 1][M - 1] - psum[N - 1][j]))
        
print(answer)