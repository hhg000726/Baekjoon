import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
dp = [[] for _ in range(M + 1)]
for i in range(len(P)):
    if P[i] < len(dp):
        dp[P[i]] = [i]
for i in range(1, M + 1):
    for j in range(len(P)):
        if i - P[j] >= 0:
            if not dp[i]:
                dp[i] = dp[i - P[j]] + [j]
                continue
            if int(''.join(list(map(str, sorted(dp[i], reverse=True))))) < int(''.join(list(map(str, sorted(dp[i - P[j]] + [j], reverse=True))))):
                dp[i] = dp[i - P[j]] + [j]
print(int(''.join(list(map(str, sorted(dp[-1], reverse=True))))))