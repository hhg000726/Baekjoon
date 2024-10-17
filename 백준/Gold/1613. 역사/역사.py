import sys
nNode, nCase = map(int, sys.stdin.readline().split())
graph = [[False for _ in range(nNode + 1)] for _ in range(nNode + 1)]
for _ in range(nCase):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
for k in range(1, nNode + 1):
    for i in range(1, nNode + 1):
        if graph[i][k]:
            for j in range(1, nNode + 1):
                if graph[k][j]:
                    graph[i][j] = True
testCases = []
for _ in range(int(sys.stdin.readline())):
    testCases.append(list(map(int, sys.stdin.readline().split())))
for i in testCases:
    if graph[i[0]][i[1]]:
        print(-1)
    elif graph[i[1]][i[0]]:
        print(1)
    else:
        print(0)