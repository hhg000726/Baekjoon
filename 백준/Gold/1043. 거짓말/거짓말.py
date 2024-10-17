import sys

N, M = map(int, sys.stdin.readline().split())

setknowing = set(list(map(int, sys.stdin.readline().split()))[1:])
party = []
answer = 0
        
for i in range(M):
    party.append(list(map(int, sys.stdin.readline().split()))[1:])

for i in range(M):
    for j in range(M):
        for k in range(len(party[j])):
            if party[j][k] in setknowing:
                setknowing = setknowing | set(party[j])
                break
                
for i in range(M):
    over = True
    for j in range(len(party[i])):
        if party[i][j] in setknowing:
            over = False
            break
    if over:
        answer += 1
        
print(answer)