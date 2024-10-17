import sys

n = int(sys.stdin.readline())
members = []
for i in range(n):
    inp = sys.stdin.readline().split()
    members.append([int(inp[0]), i, inp[1]])

members.sort()
for i in range(n):
    print(members[i][0], members[i][2])