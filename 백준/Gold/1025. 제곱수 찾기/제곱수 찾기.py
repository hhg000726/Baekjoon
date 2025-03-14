import sys

N, M = list(map(int, sys.stdin.readline().split()))
numbers = []
answers = set()
squares = {i * i for i in range(100000)}
for _ in range(N):
  numbers.append(list(map(int, sys.stdin.readline().split('\n')[0])))

for i in range(N):
  for j in range(M):
    for k in range(-8, 9):
      for l in range(-8, 9):
        if k == 0 and l == 0:
          continue
        s = str(numbers[i][j])
        x = i + k
        y = j + l
        if int(s) in squares:
            answers.add(int(s))
        while x > -1 and y > -1 and  x < N and y < M:
          s += str(numbers[x][y])
          if int(s) in squares:
            answers.add(int(s))
          x += k
          y += l
if answers:
  print(max(answers))
else:
  print(-1)