import sys

n, m = list(map(int, sys.stdin.readline().split ()))

ind = list(map(int, sys.stdin.readline().split ()))

answer = 0
while ind:
    if ind[0] - 1 > n // 2:
        gap = (n + 1) - ind[0]
        for i in range(len(ind)):
            ind[i] = (ind[i] + gap - 1) % n
    else:
        gap = ind[0] - 1
        for i in range(len(ind)):
            ind[i] -= gap + 1
            if ind[i] < 1:
                ind[i] += n
    answer += gap
    ind.pop(0)
    n -= 1

print(answer)