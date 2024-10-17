import sys

n, m = list(map(int, sys.stdin.readline().split()))
inputs = []
groups = dict()
group = [-1 for _ in range(n + 1)]
index = 0

for _ in range(m):
    inputs.append(list(map(int, sys.stdin.readline().split())))

for x, a, b in inputs:
    if x == 0:
        if group[a] == -1 and group[b] == -1:
            if a != b:
                group[a] = index
                group[b] = index
                groups[index] = {a, b}
                index += 1
            else:
                continue
        elif group[a] == -1:
            group[a] = group[b]
            groups[group[b]].add(a)
        elif group[b] == -1:
            group[b] = group[a]
            groups[group[a]].add(b)
        elif group[a] != group[b]:
            if len(groups[group[a]]) > len(groups[group[b]]):
                t = group[b]
                for i in groups[t]:
                    group[i] = group[a]
                groups[group[a]] = groups[group[a]].union(groups[t])
            else:
                t = group[a]
                for i in groups[t]:
                    group[i] = group[b]
                groups[group[b]] = groups[group[b]].union(groups[t])
    else:
        if a == b or ((group[a] == group[b]) and group[a] != -1):
            print('YES')
        else:
            print('NO')