import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

answer = 0
A.sort()
d = dict()
C = sorted(B)[::-1]
for i in range(N):
    if C[i] not in d:
        d[C[i]] = [A[i]]
    else:
        d[C[i]].append(A[i])
for i in range(N):
    answer += B[i] * d[B[i]].pop()

print(answer)