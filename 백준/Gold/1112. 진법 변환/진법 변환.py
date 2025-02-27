import sys


x, b = map(int, sys.stdin.readline().split())

answer = [0] * 100

check = False

if x < 0 and b > 0:
    x = -x
    check = True

while x != 0:
    t = 1
    c = 0
    while abs(t) < abs(x):
        t *= b
        c += 1
    if c > 0:
        t = int(t / b)
        c -= 1
    if b < 0:
        if t * x  < 0:
            answer[c + 1] += 1
            x -= t * b
        else:
            answer[c] += x // t
            x = x % t
    else:
        answer[c] += x // t
        x = x % t

for i in range(98):
    if b < 0:
        if answer[i] >= abs(b):
            answer[i + 1] += abs(b) - 1
            answer[i + 2] += 1
            answer[i] -= abs(b)
    else:
        if answer[i] >= b:
            answer[i + 1] += 1
            answer[i] -= b


while answer and answer[-1] == 0:
    answer.pop()

if not answer:
    print(0)
else:
    if check:
        print('-', end='')
    print(''.join(map(str, answer[::-1])))
