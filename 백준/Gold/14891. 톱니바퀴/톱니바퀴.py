import sys

gear = []
how = []
for _ in range(4):
    gear.append(list(map(int, list(sys.stdin.readline())[:-1])))
n = int(sys.stdin.readline())
for _ in range(n):
    how.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    a, b = how[i]
    t = [0 for _ in range(4)]
    if a == 1:
        t[0] = b
        if abs(gear[0][2] - gear[1][6]) == 1:
            t[1] = -b
            if abs(gear[1][2] - gear[2][6]) == 1:
                t[2] = b
                if abs(gear[2][2] - gear[3][6]) == 1:
                    t[3] = -b
    if a == 2:
        t[1] = b
        if abs(gear[0][2] - gear[1][6]) == 1:
            t[0] = -b
        if abs(gear[1][2] - gear[2][6]) == 1:
            t[2] = -b
            if abs(gear[2][2] - gear[3][6]) == 1:
                t[3] = b
    if a == 3:
        t[2] = b
        if abs(gear[1][2] - gear[2][6]) == 1:
            t[1] = -b
            if abs(gear[0][2] - gear[1][6]) == 1:
                t[0] = b
        if abs(gear[2][2] - gear[3][6]) == 1:
            t[3] = -b
    if a == 4:
        t[3] = b
        if abs(gear[2][2] - gear[3][6]) == 1:
            t[2] = -b
            if abs(gear[1][2] - gear[2][6]) == 1:
                t[1] = b
                if abs(gear[0][2] - gear[1][6]) == 1:
                    t[0] = -b
    for j in range(4):
        if t[j] == 1:
            gear[j] = [gear[j][-1]] + gear[j][:-1]
        if t[j] == -1:
            gear[j] = gear[j][1:] + [gear[j][0]]

answer = 0
for i in range(4):
    if gear[i][0] == 1:
        answer += 2 ** i

print(answer)