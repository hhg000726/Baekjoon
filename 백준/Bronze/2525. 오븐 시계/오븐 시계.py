import sys

h, m = list(map(int, sys.stdin.readline().split()))
c = int(sys.stdin.readline())

m += c
h += m // 60
m %= 60
h %= 24

print(h, m)