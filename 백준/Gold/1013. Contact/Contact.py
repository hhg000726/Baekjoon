import sys
T = int(sys.stdin.readline())
cases = []
for _ in range(T):
    cases.append(sys.stdin.readline())
for i in range(T):
    ew = cases[i]
    answer = "NO"
    state = "nothing"
    while ew:
        p = ew[0]
        ew = ew[1:]
        if state == "nothing":
            if p == "0":
                state = "0"
                answer = "NO"
            if p == "1":
                state = "1"
                answer = "NO"
        elif state == "0":
            if p == "0":
                break
            if p == "1":
                state = "01"
                answer = "YES"
        elif state == "01":
            if p == "0":
                state = "0"
                answer = "NO"
            if p == "1":
                state = "1"
                answer = "NO"
        elif state == "1":
            if p == "0":
                state = "10"
            if p == "1":
                break
        elif state == "10":
            if p == "0":
                state = "100"
            if p == "1":
                break
        elif state == "100":
            if p == "0":
                continue
            if p == "1":
                state = "1001"
                answer = "YES"
        elif state == "1001":
            if p == "0":
                answer = "NO"
                state = "0"
            if p == "1":
                state = "10011"
        elif state == "10011":
            if p == "0":
                state = "0a"
                answer = "NO"
            if p == "1":
                continue
        elif state == "0a":
            if p == "0":
                state = "100"
            if p == "1":
                state = "01"
                answer = "YES"
    print(answer)