from collections import defaultdict
import sys
N = int(sys.stdin.readline())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
d = defaultdict(int)
answer = [numbers.pop(0)]
for i in numbers:
    d[i] += 1
i = 0
while numbers:
    if answer[-1] + 1 != numbers[i]:
        answer.append(numbers.pop(i))
        i = 0
        continue
    else:
        i += 1
    if i == len(numbers):
        for j in range(len(answer), 0, -1):
            if answer[j - 1] + 1 != numbers[0]:
                answer.insert(j, numbers.pop(0))
                break
            if j == 1:
                answer.insert(0, numbers.pop(0))
        i = 0
print(*answer)