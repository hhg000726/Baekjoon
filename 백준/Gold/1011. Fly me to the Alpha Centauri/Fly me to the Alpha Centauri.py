import sys
from functools import cache
sys.setrecursionlimit(987654321)

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print(int((y - x - 0.1) ** (1 / 2)) + round((y - x) ** (1 / 2)))