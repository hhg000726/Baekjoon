import sys

N = int(sys.stdin.readline())
numbers = [0 for _ in range(10)]
l = len(str(N))

for i in range(l):
    if i == l - 1:
        for j in range(1, int(str(N)[0])):
            numbers[j] += 10 ** i
        numbers[int(str(N)[0])] += N % (10 ** i) + 1
    else:
        for j in range(0, int(str(N)[l - i - 1])):
            numbers[j] += (N // 10 ** (i + 1) + 1) * (10 ** i)
        numbers[int(str(N)[l - i - 1])] += (N % (10 ** i)) + 1
        for j in range(int(str(N)[l - i - 1]), 10):
            numbers[j] += (N // 10 ** (i + 1)) * (10 ** i)
        numbers[0] -= 10 ** i
        
print(*numbers)