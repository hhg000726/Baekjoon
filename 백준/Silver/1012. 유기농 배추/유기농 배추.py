import sys

t = int(sys.stdin.readline())
    
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = []

for _ in range(t):
    ret = 0
    n, m, w = list(map(int, sys.stdin.readline().split()))
    maps = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(w):
        x, y = list(map(int, sys.stdin.readline().split()))
        maps[x][y] = 1
        
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                q = [[i, j]]
                maps[i][j] = 0
                while q:
                    t = q.pop(0)
                    for k in directions:
                        if -1 < t[0] + k[0] < n and -1 < t[1] + k[1] < m and maps[t[0] + k[0]][t[1] + k[1]] == 1:
                            q.append([t[0] + k[0], t[1] + k[1]])
                            maps[t[0] + k[0]][t[1] + k[1]] = 0
                ret += 1
                
    answer.append(ret)
    
for i in answer:
    print(i)