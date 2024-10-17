import sys

N, M, x, y, K = list(map(int, sys.stdin.readline().split()))
board = []
dice = {
    'n' : 0,
    's' : 0,
    'w' : 0,
    'e' : 0,
    'floor' : 0,
    'ceil' : 0,
}


for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

move = list(map(int, sys.stdin.readline().split()))

for i in move:
    if i == 1:
        if y == M - 1:
            continue
        y += 1
        t = dice['floor']
        dice['floor'] = dice['e']
        dice['e'] = dice['ceil']
        dice['ceil'] = dice['w']
        dice['w'] = t
        if board[x][y] == 0:
            board[x][y] = dice['floor']
        else:
            dice['floor'] = board[x][y]
            board[x][y] = 0
        print(dice['ceil'])
    if i == 2:
        if y == 0:
            continue
        y -= 1
        t = dice['floor']
        dice['floor'] = dice['w']
        dice['w'] = dice['ceil']
        dice['ceil'] = dice['e']
        dice['e'] = t
        if board[x][y] == 0:
            board[x][y] = dice['floor']
        else:
            dice['floor'] = board[x][y]
            board[x][y] = 0
        print(dice['ceil'])
    if i == 3:
        if x == 0:
            continue
        x -= 1
        t = dice['floor']
        dice['floor'] = dice['n']
        dice['n'] = dice['ceil']
        dice['ceil'] = dice['s']
        dice['s'] = t
        if board[x][y] == 0:
            board[x][y] = dice['floor']
        else:
            dice['floor'] = board[x][y]
            board[x][y] = 0
        print(dice['ceil'])
    if i == 4:
        if x == N - 1:
            continue
        x += 1
        t = dice['floor']
        dice['floor'] = dice['s']
        dice['s'] = dice['ceil']
        dice['ceil'] = dice['n']
        dice['n'] = t
        if board[x][y] == 0:
            board[x][y] = dice['floor']
        else:
            dice['floor'] = board[x][y]
            board[x][y] = 0
        print(dice['ceil'])