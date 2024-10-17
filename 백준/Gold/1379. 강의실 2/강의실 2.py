import bisect

n = int(input())
lec = []

for i in range(n):
    a, start, end = list(map(int, input().split()))
    lec.append([start, end, a])

lec.sort()
ends = []
rooms = dict()

index = 1
answer = []
for i in lec:
    if ends and ends[0][0] <= i[0]:
        bisect.insort(ends, [i[1], i[2]])
        rooms[i[2]] = rooms[ends[0][1]]
        del rooms[ends[0][1]]
        answer.append([i[2], rooms[i[2]]])
        ends.pop(0)
    else:
        bisect.insort(ends, [i[1], i[2]])
        rooms[i[2]] = index
        answer.append([i[2], index])
        index += 1

print(len(rooms))
answer.sort()
for i in answer:
    print(i[1])