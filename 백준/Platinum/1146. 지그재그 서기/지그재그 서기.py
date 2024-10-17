import sys

N = int(sys.stdin.readline())
data = [[0 for _ in range(101)] for _ in range(101)]

def dp(a, b):
    if a == 1 and b == 0:
        return 1
    ret = 0
    if data[a][b] !=0:
        return data[a][b]
    for (i, j) in zip(range(b, a + b), range(a - 1, -1, -1)):
        ret += dp(i, j)
    data[a][b] = ret
    return ret

if N == 1:
    print(1)
else:
    print((2 * dp(N, 0)) % 1000000)