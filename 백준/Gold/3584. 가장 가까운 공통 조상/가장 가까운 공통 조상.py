import sys

t = int(sys.stdin.readline())
trees = []
abs = []

for i in range(t):
    n = int(sys.stdin.readline())
    trees.append([j for j in range(n + 1)])
    for _ in range(n - 1):
        a, b = list(map(int, sys.stdin.readline().split()))
        trees[i][b] = a
    abs.append(list(map(int, sys.stdin.readline().split())))
    

for i in range(t):
    a = abs[i][0]
    b = abs[i][1]
    parenta = [a]
    parentb = [b]
    while trees[i][a] != a:
        a = trees[i][a]
        parenta.append(a)
    while trees[i][b] != b:
        b = trees[i][b]
        parentb.append(b)
    x = set(parenta).intersection(set(parentb))
    for i in parenta:
        if i in x:
            print(i)
            break
        