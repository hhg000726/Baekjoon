import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

answer = set()
 
if len(numbers) == 1:
  print('A')
elif len(numbers) == 2:
  if numbers[0] == numbers[1]:
    print(numbers[0])
  else:
    print('A')
else:
  if numbers[1] == numbers[0]:
    check = True
    for i in numbers:
      if i != numbers[0]:
        print('B')
        check = False
        break
    if check:
      print(numbers[0])
  else:
    a = (numbers[2] - numbers[1]) / (numbers[1] - numbers[0])
    if a != (numbers[2] - numbers[1]) // (numbers[1] - numbers[0]):
      print('B')
    else:
      b = numbers[1] - numbers[0] * a
      check = True
      for i in range(N - 1):
        if numbers[i + 1] != numbers[i] * a + b:
          print('B')
          check = False
          break
      if check:
        print(int(numbers[-1] * a + b))