import sys
import math

x, y, d, t = map(float, sys.stdin.readline().split())
l = math.sqrt(x ** 2 + y ** 2)
answer = 0
if t < d:
    while l > 0:
        if l > 2 * d:
            l -= d
            answer += t
        else:
            answer += min(2.0 * t, l, t + abs(l - d))
            l = 0
    print(answer)
else:
    print(l)