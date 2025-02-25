import sys
from collections import deque, defaultdict

answers = []

for _ in range(int(sys.stdin.readline())):
    answer = 0
    N, K = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    maxn = max(numbers)
    mins = defaultdict(lambda: 987654321)
    results = defaultdict(lambda: 987654321)
    for i in range(N):
        mins[numbers[i]] = min(mins[numbers[i]], i)
    
    q = deque()
    for i in sorted(numbers):
        while q and q[0] < i - K:
            q.popleft()
        while q and mins[q[-1]] > mins[i]:
            q.pop()
        q.append(i)
        results[i] = mins[q[0]]
    for i in range(N):
        answer += i - results[numbers[i]]
    answers.append(answer)

for i in range(len(answers)):
    print('Case #' + str(i + 1))
    print(answers[i])