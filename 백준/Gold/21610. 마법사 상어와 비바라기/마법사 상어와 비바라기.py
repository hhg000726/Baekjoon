import sys

directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

N, M = list(map(int, sys.stdin.readline().split()))

buckets = []
infos = []

for _ in range(N):
    buckets.append(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    infos.append(list(map(int, sys.stdin.readline().split())))

goorm = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

for info in infos:
    
    new_goorm = set()
    
    for g in goorm:
        g[0] = (g[0] + directions[info[0] - 1][0] * info[1]) % N
        g[1] = (g[1] + directions[info[0] - 1][1] * info[1]) % N
        buckets[g[0]][g[1]] += 1
        new_goorm.add((g[0], g[1]))
    
    newbuckets = []
    for i in range(N):
        newbuckets.append(buckets[i][:])
    temp_goorm = []
    
    for g in goorm:
        i = g[0]
        j = g[1]
        if i > 0:
            if j > 0 and buckets[i - 1][j - 1] > 0:
                newbuckets[i][j] += 1
            if j < N - 1 and buckets[i - 1][j + 1] > 0:
                newbuckets[i][j] += 1
        if i < N - 1:
            if j > 0 and buckets[i + 1][j - 1] > 0:
                newbuckets[i][j] += 1
            if j < N - 1 and buckets[i + 1][j + 1] > 0:
                newbuckets[i][j] += 1
                
    for i in range(N):
        for j in range(N):
            if newbuckets[i][j] > 1 and (i, j) not in new_goorm:
                newbuckets[i][j] -= 2
                temp_goorm.append([i, j])
                
    goorm = temp_goorm[:]
    for i in range(N):
        buckets[i] = newbuckets[i][:]

print(sum(map(sum, buckets)))
