now = input().split()
tt = int(input())
hour = int(now[0])
mn = int(now[1])
now = mn + hour * 60 + tt
now = now % 1440
hour = int(now / 60)
mn = int(now % 60)
print(hour, mn)