import sys

N, K = map(int, sys.stdin.readline().split())

belt = list(map(int, sys.stdin.readline().split()))
robot = [False for _ in range(2 * N)]
counter = 0
stage = 0

while counter < K:
    stage += 1

    belt = [belt[-1]] + belt[:-1]
    robot = [robot[-1]] + robot[:-1]

    robot[N - 1] = False

    for i in range(N - 2, -1, -1):
        next = i + 1
        if robot[i] == True and belt[next] > 0 and robot[next] == False:
            belt[next] -= 1
            if belt[next] == 0:
                counter += 1
            robot[i] = False
            if next != N - 1:
                robot[next] = True

    if belt[0] > 0 and robot[0] == False:
        belt[0] -= 1
        if belt[0] == 0:
            counter += 1
        robot[0] = True

print(stage)