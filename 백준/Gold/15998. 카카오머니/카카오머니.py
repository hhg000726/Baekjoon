import math
import sys

n = int(sys.stdin.readline())
num = set()
maxChar = 1
dep = 0
answer = 1

for _ in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    if dep + a < 0:
        num.add(b - a - dep)
        maxChar = max(maxChar, b)
    elif dep + a != b:
        num = set()
        answer = -1
        break
    dep = b

if num:
    answer = list(num)[0]

for i in num:
    t = math.gcd(i, answer)
    if t > maxChar:
        answer = t
    else:
        answer = -1
        break

print(answer)