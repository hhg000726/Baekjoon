import sys

N = int(sys.stdin.readline())
strs = []
for _ in range(N):
  strs.append(sys.stdin.readline())

answer = ""

for i in range(len(strs[0])):
  t = True
  for j in range(N - 1):
    if strs[j][i] != strs[j + 1][i]:
      answer += "?"
      t = False
      break
  if t:
    answer += strs[0][i]

print(answer)