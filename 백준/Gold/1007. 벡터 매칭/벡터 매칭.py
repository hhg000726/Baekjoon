import itertools
import math
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    answer = 987654321
    P = []
    N = int(sys.stdin.readline())
    for _ in range(N):
        P.append(list(map(int, sys.stdin.readline().split())))
    total = [sum(col) for col in zip(*P)]
    combs = list(itertools.combinations(P, int(N / 2)))
    sums = [[sum(col) for col in zip(*comb)] for comb in combs]
    for i in sums:
        answer = min(answer, math.sqrt((total[0] - 2 * i[0]) ** 2 + (total[1] - 2 * i[1]) ** 2))
    print(answer)