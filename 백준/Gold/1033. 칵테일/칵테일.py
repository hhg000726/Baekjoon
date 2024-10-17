import sys
import math

N = int(sys.stdin.readline())
ingredients = [0 for _ in range(N)]
group = dict()
wheregroup = dict()

g = 0
for _ in range(N - 1):
    a, b, p, q = map(int, sys.stdin.readline().split())
    if ingredients[a] == 0 and ingredients[b] == 0:
        ingredients[a] = p
        ingredients[b] = q
        wheregroup[a] = g
        wheregroup[b] = g
        group[g] = [a, b]
        g += 1
    elif ingredients[a] == 0:
        ingredients[a] = ingredients[b] * p
        for i in group[wheregroup[b]]:
            ingredients[i] *= q
        wheregroup[a] = wheregroup[b]
        group[wheregroup[b]].append(a)
    elif ingredients[b] == 0:
        ingredients[b] = ingredients[a] * q
        for i in group[wheregroup[a]]:
            ingredients[i] *= p
        wheregroup[b] = wheregroup[a]
        group[wheregroup[a]].append(b)
    else:
        x = ingredients[a]
        y = ingredients[b]
        delGroup = wheregroup[b]
        for i in group[wheregroup[a]]:
            ingredients[i] *= y * p
        for i in group[wheregroup[b]]:
            ingredients[i] *= x * q
            wheregroup[i] = wheregroup[a]
            group[wheregroup[a]].append(i)
        del(group[delGroup])

d = ingredients[0]
for i in range(1, N):
    d = math.gcd(d, ingredients[i])
    
for i in range(N):
    ingredients[i] = int(ingredients[i] / d)
    
for i in range(N):
    print(ingredients[i], end = " ")