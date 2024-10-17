bt = input().split()
bt = (int(bt[0]) * 60 + int(bt[1]) + 1440 - 45) % 1440
print(int(bt/60),bt%60)