import sys

T = int(sys.stdin.readline())
results = []
for _ in range(T):
    hp, mp, atk, df, hpp, mpp, atkp, dfp = list(map(int, sys.stdin.readline().split()))
    results.append(max(1, hp + hpp) + max(1, mp + mpp) * 5 + max(0, atk +atkp) * 2 + (df + dfp) * 2)

for result in results:
    print(result)