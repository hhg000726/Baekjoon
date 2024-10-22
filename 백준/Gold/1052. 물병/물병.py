import sys

n, k = list(map(int, sys.stdin.readline().split()))

def tobin(n):
    l = []
    while n > 0:
        if n % 2 == 0:
            l.append(0)
        else:
            l.append(1)
        n = n // 2
    return l

def todec(l):
    n = 0
    for i in range(len(l)):
        n += l[i] * 2 ** i
    return n

nbin = tobin(n)
original_count = sum(nbin)
i = original_count - k + 1
if i > 1:
    ind = -1
    for j in range(len(nbin)):
        if nbin[j] == 1:
            i -= 1
        if i == 0:
            ind = j
            break
    if ind == -1:
        print(-1)
    else:
        print(2 ** (ind + 1) - todec(nbin[:ind + 1]))
else:
    print(0)