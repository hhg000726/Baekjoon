import sys

C = int(sys.stdin.readline())
N = int(sys.stdin.readline())
price = [[987654321 for _ in range(C + 1)] for _ in range(C + 1)]
for i in range(N):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    if c < price[a][b]:
        price[a][b] = c

for by in range(1, C + 1):
    for start in range(1, C + 1):
        for end in range(1, C +1):
            if start != end and price[start][end] > price[start][by] + price[by][end]:
                price[start][end] = price[start][by] + price[by][end]

for i in range(1, C + 1):
    for j in range(1, C + 1):
        if price[i][j] == 987654321 or i == j:
            price[i][j] = 0
            
for i in range(1, C + 1):
    print(*price[i][1:])