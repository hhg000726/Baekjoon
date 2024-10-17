import sys
N = int(sys.stdin.readline())
p = []
answer = [[10, 10], [1, 1], [6, 2, 4, 8, 6], [1, 3, 9, 7, 1], [6, 4, 6], [5, 5], [6, 6], [1, 7, 9, 3, 1], [6, 8, 4, 2, 6], [1, 9, 1]] * 11
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    p.append([a, b])
for i in p:
    print(answer[i[0]][i[1] % (len(answer[i[0]]) - 1)])