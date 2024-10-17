import sys
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
for i in nums:
    a = [1, 0]
    b = [0, 1]
    for _ in range(i):
        a, b = [b[0], b[1]], [a[0] + b[0], a[1] + b[1]]
    print(a[0], a[1])