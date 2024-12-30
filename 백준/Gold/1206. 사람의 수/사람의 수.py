import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
  nums.append(int(sys.stdin.readline().split('.')[1]))

a = 0
i = 1
while a < len(nums):
  for n in nums:
    if n * i == ((n * i) // 1000) * 1000 or ((n + 1) * i != (((n + 1) * i) // 1000) * 1000 and (n * i) // 1000 != ((n + 1) * i) // 1000):
      a += 1
    else:
      i += 1
      a = 0
      break
  
print(i)