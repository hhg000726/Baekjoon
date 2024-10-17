import sys

min, max = map(int, sys.stdin.readline().split())
jgs = []
answer = max - min + 1

check = [False for _ in range(999999)]
for i in range(2, 1000001):
    j = i
    if check[j - 2] == False:
        jgs.append(i ** 2)
        while j <= 1000000:
            if check[j - 2] == False:
                check[j - 2] = True
            j += i
        
check = [False for _ in range(max - min + 1)]
for i in range(len(jgs)):
    x = min % jgs[i]
    if x == 0:
        j = min
    else:
        j = min + jgs[i] - x
    while min <= j <= max:
        if check[j - min] == False:
            check[j - min] = True
            answer -= 1
        j += jgs[i]

print(answer)