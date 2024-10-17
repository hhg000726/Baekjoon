import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(math.comb(b, a))